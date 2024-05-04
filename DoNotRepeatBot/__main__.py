"""Starts the bot."""

import logging
from os import getenv

from telegram.constants import ParseMode
from telegram.ext import Application, ApplicationBuilder, Defaults

from DoNotRepeatBot.commands import commands
from DoNotRepeatBot.constants import Literal
from DoNotRepeatBot.handlers import handlers
from DoNotRepeatBot.utils import Database, GetText

TOKEN = getenv("TOKEN", "")
DATABASE_URL = getenv("DATABASE_URL", "")

INTERVAL = int(getenv("INTERVAL", 2))

LISTEN = getenv("LISTEN", "0.0.0.0")
PORT = int(getenv("PORT", 80))
URL_PATH = getenv("URL_PATH", "")
WEBHOOK_URL = getenv("WEBHOOK_URL")


async def post_init(application: Application):
    application.bot_data["database"] = Database(DATABASE_URL)
    application.bot_data["gettext"] = GetText()

    for group, handlers_lx in handlers.items():
        application.add_handlers(handlers_lx, group)

    for scope, cmds in commands.items():
        await application.bot.set_my_commands(commands=cmds, scope=scope)


async def post_shutdown(application: Application):
    del application.bot_data["database"]


logging.basicConfig(
    format="%(asctime)s - %(name)s:%(levelname)s - %(message)s",
    level=logging.INFO,
)
logging.getLogger("httpx").setLevel(logging.WARNING)

application = (
    ApplicationBuilder()
    .defaults(Defaults(parse_mode=ParseMode.HTML, do_quote=True))
    .post_init(post_init)
    .post_shutdown(post_shutdown)
    .token(TOKEN)
    .build()
)

if WEBHOOK_URL:
    application.run_webhook(
        listen=LISTEN,
        port=PORT,
        url_path=URL_PATH,
        webhook_url=WEBHOOK_URL,
        allowed_updates=Literal.UPDATES,
    )
else:
    application.run_polling(poll_interval=INTERVAL, allowed_updates=Literal.UPDATES)
