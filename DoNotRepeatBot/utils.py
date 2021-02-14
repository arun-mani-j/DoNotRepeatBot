"""
Functions used for specific operations.
"""

from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.constants import (
    CHATMEMBER_ADMINISTRATOR,
    CHATMEMBER_CREATOR,
    CHAT_GROUP,
    CHAT_SUPERGROUP,
)
from telegram.ext import CallbackContext
from .message import Message


def is_admin(func):

    """
    Wrapper to check if the update is from an admin.
    """

    def wrapped(update: Update, context: CallbackContext):

        if update.message.chat.type in (CHAT_GROUP, CHAT_SUPERGROUP):
            mem = update.message.chat.get_member(user_id=update.message.from_user.id)
            if mem.status not in (CHATMEMBER_ADMINISTRATOR, CHATMEMBER_CREATOR):
                update.message.reply_html(text=Message.INVALID_PERMISSIONS, quote=True)
                return
        func(update, context)

    return wrapped
