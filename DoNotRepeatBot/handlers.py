"""
Handlers for incoming updates from Telegram
"""
import logging
from telegram import (
    ForceReply,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Update,
)
from telegram.constants import PARSEMODE_HTML
from telegram.error import BadRequest
from telegram.ext import CallbackContext
from .message import Message
from .utils import is_admin


def _add(update: Update, context: CallbackContext):

    """
    Parses the given text messages and adds/updates it in database.
    """

    database = context.bot_data["database"]
    chat_id = update.message.chat.id
    title = context.user_data.pop("snippetTitle")
    snippet = update.message.text_html_urled
    ret = database.add_snippet(chat_id, title, snippet)

    if ret:
        text = Message.ADDED_SNIPPET.format(TITLE=title)
    else:
        text = Message.UPDATED_SNIPPET.format(TITLE=title)

    # TODO With the current table structure, there is no way to know if it was addition or updation.
    # So everytime, it is always an addition.

    update.message.reply_html(text=text, quote=True)


@is_admin
def add(update: Update, context: CallbackContext):

    """
    Prompts the user to send the snippet to save.
    """

    title = " ".join(context.args)

    if title:
        context.user_data["snippetTitle"] = title
        context.user_data["addSnippet"] = True
        text = Message.ADD
        reply_markup = ForceReply(force_reply=True, selective=True)
    else:
        text = Message.EMPTY_TITLE
        reply_markup = None

    update.message.reply_html(text=text, quote=True, reply_markup=reply_markup)


@is_admin
def delete(update: Update, context: CallbackContext):

    """
    Deletes the snippet whose title is given as argument.
    """

    database = context.bot_data["database"]
    chat_id = update.message.chat.id
    title = " ".join(context.args)

    if not title:
        update.message.reply_html(text=Message.NO_TITLE, quote=True)
        return

    ret = database.remove_snippet(chat_id, title)

    if ret:
        text = Message.DELETED_SNIPPET.format(TITLE=title)
    else:
        text = Message.DELETED_NONE.format(TITLE=title)

    update.message.reply_html(text=text, quote=True)


def find_inline(update: Update, context: CallbackContext):

    """
    Searches the snippets matching the given inline query phrase.\
    Presents a list of recently used snippets for empty keyword.
    """

    database = context.bot_data["database"]
    query = update.inline_query
    chat_id = query.from_user.id
    keyword = query.query
    results = []

    for title, snippet in database.find_snippets(chat_id, keyword):
        content = InputTextMessageContent(
            message_text=snippet, parse_mode=PARSEMODE_HTML
        )
        article = InlineQueryResultArticle(
            id=title[:64],
            title=title,
            input_message_content=content,
            description=snippet,
        )
        results.append(article)

    if keyword:
        context.user_data["toAddTitle"] = keyword
        kwargs = {
            "switch_pm_text": Message.SWITCH_PM,
            "switch_pm_parameter": "addSnippet",
        }
    else:
        kwargs = {}

    query.answer(results=results, cache_time=5, is_personal=True, **kwargs)


def find_text(update: Update, context: CallbackContext):

    """
    Send the snippet asked via hash-tag text.
    """

    database = context.bot_data["database"]
    chat_id = update.message.chat.id
    title = update.message.text[1:]

    if not title:
        return

    _, snippet = next(database.find_snippets(chat_id, title, 1), (None, None))

    if not snippet:
        update.message.reply_html(text=Message.NO_RESULTS, quote=True)
        return

    if update.message.reply_to_message:
        update.message.reply_to_message.reply_html(text=snippet, quote=True)
    else:
        update.message.reply_html(text=snippet, quote=False)

    try:
        update.message.delete()
    except BadRequest:
        pass


def handle_text(update: Update, context: CallbackContext):

    """
    Adds the snippet if it was meant to be.
    """

    if update.message.reply_to_message.from_user.id != context.bot.id:
        return

    if context.user_data.pop("addSnippet", False):
        _add(update, context)
    else:
        update.message.reply_html(text=Message.UNEXPECTED_MESSAGE, quote=True)


def help_info(update: Update, _: CallbackContext):

    """
    Sends the help message.
    """

    update.message.reply_html(text=Message.HELP, quote=True)


def snippets(update: Update, context: CallbackContext):

    """
    Shows all the titles of snippets by user.
    """

    database = context.bot_data["database"]
    chat_id = update.message.chat.id
    titles = (
        Message.SNIPPET_ITEM.format(TITLE=title)
        for (title,) in database.list_snippets(chat_id)
    )
    titles_text = "\n".join(titles)

    if titles_text:
        text = Message.SNIPPETS.format(TITLES=titles_text)
    else:
        text = Message.NO_SNIPPETS

    update.message.reply_html(text=text, quote=True)


def start(update: Update, context: CallbackContext):

    """
    Starts the bot for user.
    """

    if context.args and context.args[0] == "addSnippet":
        context.args = context.user_data.pop("toAddTitle").split()
        add(update, context)
    else:
        update.message.reply_html(text=Message.START, quote=True)


def stay_awake_ping(_, __):

    """
    Logs that ping received successfully.
    """

    logging.info("Got ping to stay awake")


def update_usage(update: Update, context: CallbackContext):

    """
    Increments the usage of chosen inline result's article by one.
    """

    database = context.bot_data["database"]
    title = update.chosen_inline_result.result_id
    chat_id = update.chosen_inline_result.from_user.id
    database.update_snippet_usage(chat_id, title)
