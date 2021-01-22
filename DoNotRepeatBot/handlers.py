"""
Handlers for incoming updates from Telegram
"""
import logging
from telegram import ParseMode, Update
from telegram.ext import CallbackContext
from .message import Message
from .utils import get_common_results, get_results


def _add(update: Update, context: CallbackContext):

    """
    Parses the given text messages and adds/updates it in database.
    """

    database = context.bot_data["database"]
    user_id = update.message.from_user.id
    title = context.user_data.pop("snippetTitle")
    snippet = update.message.text_html_urled
    ret = database.add_snippet(user_id, title, snippet)

    if ret:
        text = Message.ADDED_SNIPPET.format(TITLE=title)
    else:
        text = Message.UPDATED_SNIPPET.format(TITLE=title)

    # TODO With the current table structure, there is no way to know if it was addition or updation.
    # So everytime, it is always an addition.

    update.message.reply_text(text=text, parse_mode=ParseMode.HTML)


def handle_text(update: Update, context: CallbackContext):

    """
    Adds the snippet if it was meant to be.
    """

    if not update.message:
        logging.info("Got ping to stay awake")
        return

    if context.user_data.pop("addSnippet", False):
        _add(update, context)
    else:
        update.message.reply_text(
            text=Message.UNEXPECTED_MESSAGE, parse_mode=ParseMode.HTML
        )


def add(update: Update, context: CallbackContext):

    """
    Prompts the user to send the snippet to save.
    """

    title = " ".join(context.args)

    if title:
        context.user_data["snippetTitle"] = title
        context.user_data["addSnippet"] = True
        text = Message.ADD
    else:
        text = Message.EMPTY_TITLE

    update.message.reply_text(text=text, parse_mode=ParseMode.HTML)


def delete(update: Update, context: CallbackContext):

    """
    Deletes the snippet whose title is given as argument.
    """

    database = context.bot_data["database"]
    user_id = update.message.from_user.id
    title = " ".join(context.args)

    if not title:
        update.message.reply_text(text=Message.NO_TITLE, parse_mode=ParseMode.HTML)
        return

    ret = database.remove_snippet(user_id, title)

    if ret:
        text = Message.DELETED_SNIPPET.format(TITLE=title)
    else:
        text = Message.DELETED_NONE.format(TITLE=title)

    update.message.reply_text(text=text, parse_mode=ParseMode.HTML)


def find(update: Update, context: CallbackContext):

    """
    Searches the snippets matching the given phrase.
    """

    database = context.bot_data["database"]
    query = update.inline_query
    user_id = query.from_user.id
    keyword = query.query

    if keyword:
        results = get_results(database, user_id, keyword)
        context.user_data["toAddTitle"] = keyword
        kwargs = {
            "switch_pm_text": Message.SWITCH_PM,
            "switch_pm_parameter": "addSnippet",
        }
    else:
        results = get_common_results(database)
        kwargs = {}

    query.answer(results=results, cache_time=5, is_personal=True, **kwargs)


def help_info(update: Update, _: CallbackContext):

    """
    Sends the help message.
    """

    update.message.reply_text(text=Message.HELP, parse_mode=ParseMode.HTML)


def snippets(update: Update, context: CallbackContext):

    """
    Shows all the titles of snippets by user.
    """

    database = context.bot_data["database"]
    user_id = update.message.from_user.id
    titles = (
        Message.SNIPPET_ITEM.format(TITLE=title)
        for title in database.list_snippets(user_id)
    )
    titles_text = "\n".join(titles)

    if titles_text:
        text = f"{Message.SNIPPETS}\n{titles_text}"
    else:
        text = Message.NO_SNIPPETS

    update.message.reply_text(text=text, parse_mode=ParseMode.HTML)


def start(update: Update, context: CallbackContext):

    """
    Starts the bot for user.
    """

    if context.args and context.args[0] == "addSnippet":
        context.args = context.user_data.pop("toAddTitle").split()
        add(update, context)
    else:
        update.message.reply_text(
            text=Message.START, parse_mode=ParseMode.HTML, quote=False
        )
