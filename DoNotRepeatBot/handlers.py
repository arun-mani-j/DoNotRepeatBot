"""Handlers for various functionalities."""

import re

from telegram import Update
from telegram.ext import (ChatMemberHandler, ChosenInlineResultHandler,
                          CommandHandler, InlineQueryHandler, MessageHandler,
                          TypeHandler)
from telegram.ext.filters import Filters

from DoNotRepeatBot.base.command import (add, clear, del_, done, get, guide,
                                         help_, import_, lang, list_, start,
                                         stats)
from DoNotRepeatBot.base.inlinequery import increment, search
from DoNotRepeatBot.base.message import fallback, hashtag
from DoNotRepeatBot.base.preference import initiate, tweak

# (Handler, (dispatcher_args)) : [(handler_args),]
handlers = {
    (ChatMemberHandler, ()): [(initiate,)],
    (ChosenInlineResultHandler, ()): [(increment,)],
    (CommandHandler, ()): [
        ("add", add),
        ("clear", clear),
        ("del", del_),
        ("done", done),
        ("get", get),
        ("guide", guide),
        ("help", help_),
        ("import", import_),
        ("lang", lang),
        ("list", list_),
        ("start", start),
        ("stats", stats),
    ],
    (InlineQueryHandler, ()): [(search,)],
    (MessageHandler, ()): [
        (Filters.regex(r"^#\w+$"), hashtag),
        (~Filters.command & ~Filters.status_update, fallback),
    ],
    (TypeHandler, (-10,)): [(Update, tweak)],
}
