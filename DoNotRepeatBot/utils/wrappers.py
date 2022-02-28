"""Wrappers used for specific operations."""

from telegram import Update
from telegram.ext import CallbackContext

from DoNotRepeatBot.constants import Message


def _private_or_admin(update: Update, context: CallbackContext, silent: bool = True):
    """Check if user is an admin or chat is private and warn if silent is False."""
    chat = update.message.chat
    user = update.message.from_user.id
    if chat.type != chat.PRIVATE:
        mem = chat.get_member(user_id=user)
        if mem.status not in (mem.ADMINISTRATOR, mem.CREATOR):
            if not silent:
                update.message.reply_html(text=Message.INVALID_PERMISSIONS, quote=True)
            return False
    return True


def is_admin(func):
    """Wrapper to check if the update is from an admin or private chat."""

    def wrapped(update: Update, context: CallbackContext):
        if _private_or_admin(update, context, False):
            func(update, context)

    return wrapped


def is_admin_silent(func):
    """Wrapper to check if the update is from an admin or private chat silently."""

    def wrapped(update: Update, context: CallbackContext):
        if _private_or_admin(update, context):
            func(update, context)

    return wrapped
