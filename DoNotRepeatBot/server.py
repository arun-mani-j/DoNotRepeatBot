"""
Contains Server object which obtains the updates and distributes them to handlers.
"""

import logging
from os import getenv
from telegram.ext import (
    Filters,
    CommandHandler,
    InlineQueryHandler,
    MessageHandler,
    Updater,
)
from .database import Database
from .handlers import add, delete, find, handle_text, help_info, snippets, start

DATABASE_URL = getenv("DATABASE_URL")
LISTEN = getenv("LISTEN")
PORT = int(getenv("PORT", "0"))
TOKEN = getenv("TOKEN")
URL = getenv("URL")


class Server:
    def __init__(self):

        """
        Server uses Updater to handle different updates from Telegram.
        The bot token, taken as TOKEN and database URL, \
        taken as DATABASE_URL are obtained from environment variables.
        """

        self.updater = Updater(token=TOKEN, user_sig_handler=self.sig_handler)
        self.database = Database(DATABASE_URL)
        dispatcher = self.updater.dispatcher
        dispatcher.bot_data["database"] = self.database

        for (cmd, hdr) in (
            ("add", add),
            ("del", delete),
            ("help", help_info),
            ("snippets", snippets),
            ("start", start),
        ):
            dispatcher.add_handler(CommandHandler(cmd, hdr))
        dispatcher.add_handler(InlineQueryHandler(find))
        dispatcher.add_handler(
            MessageHandler(filters=Filters.text, callback=handle_text)
        )

    def listen(self):

        """
        Starts webhook on the URL obtained from environment variable.
        """

        self.updater.start_webhook(
            listen=LISTEN,
            port=PORT,
            url_path=TOKEN,
            allowed_updates=["channel_post","inline_query", "message"],
        )
        self.updater.bot.set_webhook(f"{URL}/{TOKEN}")
        logging.info("Started listening")
        self.updater.idle()

    def poll(self):

        """
        Starts polling for updates.
        """

        self.updater.start_polling(allowed_updates=["channel_post", "inline_query", "message"])
        logging.info("Started polling")
        self.updater.idle()

    def sig_handler(self, *_):

        """
        Closes the connection to database.
        """

        del self.updater.dispatcher.bot_data["database"]
        logging.info("Shutting down. Bye.")
