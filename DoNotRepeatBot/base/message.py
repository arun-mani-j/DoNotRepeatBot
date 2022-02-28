"""Handlers for non-command messages."""

from telegram import Update
from telegram.ext import CallbackContext

from DoNotRepeatBot.base.command import get
from DoNotRepeatBot.utils.misc import add_snippet
from DoNotRepeatBot.utils.wrappers import is_admin_silent


@is_admin_silent
def fallback(update: Update, context: CallbackContext):
    """Fallback handler for non-command messages."""
    database = context.bot_data["database"]
    gettext = context.bot_data["gettext"]
    pendingInput = context.chat_data.pop("pendingInput", False)
    title = context.chat_data.pop("title", None)
    importing = context.chat_data.get("importing", False)
    added = False

    if pendingInput or importing:
        added = add_snippet(update.message, database, gettext, title)

    if not pendingInput and importing:
        if added:
            context.chat_data["imported"] += 1
        else:
            context.chat_data["failed"] += 1


def hashtag(update: Update, context: CallbackContext):
    """Get a snippet based on hashtag title."""
    title = update.message.text[1:]
    if update.message.reply_to_message:
        update.message = update.message.reply_to_message
    context.args = (title,)
    get(update, context)
