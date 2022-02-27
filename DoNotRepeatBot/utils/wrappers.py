"""Wrappers used for specific operations."""

from telegram import Update
from telegram.ext import CallbackContext

from DoNotRepeatBot.constants import Message


def is_admin(func):
    """Wrapper to check if the update is from an admin or private chat."""

    def wrapped(update: Update, context: CallbackContext):
        chat = update.message.chat
        user = update.message.from_user.id
        if chat.type != chat.PRIVATE:
            mem = chat.get_member(user_id=user)
            if mem.status not in (mem.ADMINISTRATOR, mem.CREATOR):
                update.message.reply_html(text=Message.INVALID_PERMISSIONS, quote=True)
                return
        func(update, context)

    return wrapped
