"""Handlers for various functionalities."""

import re

from telegram import Update
from telegram.ext import (
    BaseHandler,
    ChatMemberHandler,
    ChosenInlineResultHandler,
    CommandHandler,
    InlineQueryHandler,
    MessageHandler,
    TypeHandler,
    filters,
)

from DoNotRepeatBot.base.command import (
    add,
    clear,
    del_,
    done,
    get,
    guide,
    help_,
    import_,
    lang,
    list_,
    start,
    stats,
)
from DoNotRepeatBot.base.inlinequery import increment, search
from DoNotRepeatBot.base.message import fallback, hashtag
from DoNotRepeatBot.base.preference import initiate, tweak

handlers: dict[int, list[BaseHandler]] = {
    0: [ChatMemberHandler(initiate)]
    + [ChosenInlineResultHandler(increment)]
    + [
        CommandHandler(cmd, func)
        for (cmd, func) in [
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
        ]
    ]
    + [InlineQueryHandler(search)]
    + [
        MessageHandler(fltr, func)
        for (fltr, func) in [
            (filters.Regex(r"^#\w+$"), hashtag),
            (~filters.Command() & ~filters.StatusUpdate.ALL, fallback),
        ]
    ],
    -10: [TypeHandler(Update, tweak)],
}
