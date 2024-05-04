"""Wrappers used for specific operations."""

from typing import Awaitable, Callable

from telegram import Update
from telegram.ext import CallbackContext

from DoNotRepeatBot.constants import Message


async def _private_or_admin(
    update: Update, context: CallbackContext, silent: bool = True
):
    """Check if user is an admin or chat is private and warn if silent is False."""

    if not update.message:
        raise RuntimeError()
    if not update.message.from_user:
        raise RuntimeError()

    chat = update.message.chat
    user = update.message.from_user.id
    if chat.type != chat.PRIVATE:
        mem = await chat.get_member(user_id=user)
        if mem.status not in (mem.ADMINISTRATOR, mem.OWNER):
            if not silent:
                await update.message.reply_html(
                    text=Message.INVALID_PERMISSIONS, quote=True
                )
            return False
    return True


def is_admin(func: Callable[[Update, CallbackContext], Awaitable]):
    """Wrapper to check if the update is from an admin or private chat."""

    async def wrapped(update: Update, context: CallbackContext):
        if await _private_or_admin(update, context, False):
            await func(update, context)

    return wrapped


def is_admin_silent(func: Callable[[Update, CallbackContext], Awaitable]):
    """Wrapper to check if the update is from an admin or private chat silently."""

    async def wrapped(update: Update, context: CallbackContext):
        if await _private_or_admin(update, context):
            await func(update, context)

    return wrapped
