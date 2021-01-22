"""
Functions used for specific operations.
"""

from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.constants import CHATMEMBER_ADMINISTRATOR, CHATMEMBER_CREATOR, CHAT_GROUP
from telegram.ext import CallbackContext
from .message import Message


def get_common_results(database):

    """
    Gets common results that is not specific to any user.
    """

    results = []

    for title, snippet in database.get_common_snippets():
        content = InputTextMessageContent(message_text=snippet, parse_mode="HTML")
        article = InlineQueryResultArticle(
            id=title[:64],
            title=title,
            input_message_content=content,
            description=snippet,
        )
        results.append(article)

    return results


def is_admin(func):

    """
    Wrapper to check if the update is from an admin.
    """

    def wrapped(update: Update, context: CallbackContext):

        if update.message.chat.type == CHAT_GROUP:
            mem = update.message.chat.get_member(user_id=update.message.from_user.id)
            if mem.status not in (CHATMEMBER_ADMINISTRATOR, CHATMEMBER_CREATOR):
                update.message.reply_html(text=Message.INVALID_PERMISSIONS, quote=True)
                return
        func(update, context)

    return wrapped
