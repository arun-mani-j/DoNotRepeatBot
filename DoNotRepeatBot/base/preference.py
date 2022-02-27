"""Handlers of preferences and tweaks."""

from telegram import Update
from telegram.ext import CallbackContext

from DoNotRepeatBot.constants import Literal


def initiate(update: Update, context: CallbackContext):
    """Initiate the settings"""
    database = context.bot_data["database"]
    chat = update.my_chat_member.chat
    mem = update.my_chat_member.old_chat_member
    user = update.my_chat_member.from_user

    if mem.status in (mem.KICKED, mem.RESTRICTED):
        return

    if chat.type == chat.PRIVATE:
        database.add_chat(chat.id, user.language_code)
    else:
        database.add_chat(chat.id, Literal.DEFAULT_LANG)


def tweak(update: Update, context: CallbackContext):
    """Set preferences of a chat for the update."""
    database = context.bot_data["database"]
    gettext = context.bot_data["gettext"]
    chat_id = (
        update.inline_query.from_user.id
        if update.inline_query
        else update.message.chat.id
        if update.message
        else None
    )

    lang = database.get_language(chat_id)

    if lang:
        gettext.set_language(lang)
    else:
        gettext.set_language(Literal.DEFAULT_LANG)
