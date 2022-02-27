"""Handlers for commands."""

from telegram import Update
from telegram.ext import CallbackContext

from DoNotRepeatBot.constants import Literal
from DoNotRepeatBot.utils.misc import add_snippet
from DoNotRepeatBot.utils.wrappers import is_admin


@is_admin
def add(update: Update, context: CallbackContext):
    """Add a new snippet. The snippet is taken from reply \
    else taken from next message."""
    database = context.bot_data["database"]
    gettext = context.bot_data["gettext"]
    reply = update.message.reply_to_message
    title = " ".join(context.args) if context.args else None

    if reply:
        add_snippet(reply, database, gettext, title)
    else:
        context.chat_data["pendingInput"] = True
        context.chat_data["title"] = title
        update.message.reply_text(gettext.SEND_SNIPPET)


@is_admin
def clear(update: Update, context: CallbackContext):
    """Clear all snippets of a chat."""
    database = context.bot_data["database"]
    gettext = context.bot_data["gettext"]
    database.clear_snippets(update.message.chat.id)
    update.message.reply_text(gettext.CLEARED_SNIPPETS)


@is_admin
def del_(update: Update, context: CallbackContext):
    """Delete a snippet by title."""
    database = context.bot_data["database"]
    gettext = context.bot_data["gettext"]
    title = " ".join(context.args) if context.args else None
    chat_id = update.message.chat.id

    if database.delete_snippet(chat_id, title):
        update.message.reply_text(gettext.DELETED_SNIPPET.format(TITLE=title))
    else:
        update.message.reply_text(gettext.SNIPPET_NOT_FOUND.format(TITLE=title))


@is_admin
def done(update: Update, context: CallbackContext):
    """Finish import of snippets."""
    gettext = context.bot_data["gettext"]
    context.chat_data.pop("importing", None)
    imported = context.chat_data.pop("imported", 0)
    failed = context.chat_data.pop("failed", 0)
    total = imported + failed
    update.message.reply_text(
        gettext.IMPORT_DONE.format(IMPORTED=imported, FAILED=failed, TOTAL=total)
    )


def get(update: Update, context: CallbackContext, use_id=False):
    """Get a snippet by title or ID if use ID is True."""
    database = context.bot_data["database"]
    gettext = context.bot_data["gettext"]
    chat_id = update.message.chat.id
    ident = " ".join(context.args) if context.args else None

    if use_id:
        snippet = database.get_snippet_by_id(ident)
    else:
        snippet = database.get_snippet_by_title(chat_id, ident)

    if snippet:
        func, kwargs = snippet.to_sendable(update.message)
        func(**kwargs)
    else:
        update.message.reply_text(gettext.SNIPPET_NOT_FOUND.format(TITLE=ident))


def guide(update: Update, context: CallbackContext):
    """Send guide message."""
    gettext = context.bot_data["gettext"]
    update.message.reply_text(gettext.GUIDE)


def help_(update: Update, context: CallbackContext):
    """Send help message."""
    gettext = context.bot_data["gettext"]
    update.message.reply_text(gettext.HELP)


@is_admin
def import_(update: Update, context: CallbackContext):
    """Start import of multiple snippets."""
    gettext = context.bot_data["gettext"]
    context.chat_data["importing"] = True
    context.chat_data.setdefault("imported", 0)
    context.chat_data.setdefault("failed", 0)
    update.message.reply_text(gettext.IMPORT_STARTED)


@is_admin
def lang(update: Update, context: CallbackContext):
    """Set language of bot for a chat."""
    database = context.bot_data["database"]
    gettext = context.bot_data["gettext"]
    lang = "_".join(context.args) if context.args else None
    langs = Literal.TRANSLATIONS

    if lang in langs:
        database.set_language(update.message.chat.id, lang)
        update.message.reply_text(gettext.SET_LANGUAGE.format(LANG=lang))
    else:
        update.message.reply_text(gettext.LANGUAGES.format(LANGS=langs))


def list_(update: Update, context: CallbackContext):
    """List all snippets for a chat."""
    database = context.bot_data["database"]
    gettext = context.bot_data["gettext"]
    link = context.bot.link
    snips = database.list_snippets(update.message.chat.id)
    if not snips:
        update.message.reply_text(gettext.NO_SNIPPETS)
        return

    for start in range(0, len(snips), Literal.MAX_LIST_SIZE):
        slce = snips[start : start + Literal.MAX_LIST_SIZE]
        items = (
            gettext.LIST_ITEM.format(
                LINK=link, ID=Literal.PAYLOAD_ID, LOAD=idx, TITLE=title
            )
            for (idx, title) in slce
        )
        text = "\n".join(items)
        update.message.reply_text(text)


def start(update: Update, context: CallbackContext):
    """Send start message normally, else respond to payload."""
    database = context.bot_data["database"]
    gettext = context.bot_data["gettext"]
    database.add_chat(update.message.chat.id, Literal.DEFAULT_LANG)

    if not context.args:
        update.message.reply_text(gettext.START)
        return

    arg = " ".join(context.args)

    if arg.startswith(Literal.PAYLOAD_ID):
        context.args = (arg.lstrip(Literal.PAYLOAD_ID),)
        get(update, context, True)
    elif arg == Literal.PAYLOAD_ADD:
        context.args = ()
        add(update, context)
    else:
        update.message.reply_text(gettext.INVALID_START)


def stats(update: Update, context: CallbackContext):
    """Send statistics of usage of a chat."""
    database = context.bot_data["database"]
    gettext = context.bot_data["gettext"]
    chat_id = update.message.chat.id
    count = database.get_snippets_count(chat_id)
    lang = database.get_language(chat_id)
    update.message.reply_text(
        gettext.STATS.format(CHAT_ID=chat_id, COUNT=count, LANG=lang)
    )
