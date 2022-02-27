"""Miscellaneous functions."""

from telegram import Message

from DoNotRepeatBot.utils import Database, GetText, Snippet


def add_snippet(
    message: Message, database: Database, gettext: GetText, title: str = None
) -> bool:
    """Add a new snippet from given message.
    Return True if added else False."""
    try:
        snippet = Snippet.from_message(message, title)
    except Exception as e:
        message.reply_text(gettext.get(str(e)))
        return False
    else:
        database.add_snippet(snippet)
        message.reply_text(gettext.ADDED_SNIPPET.format(TITLE=snippet.title))
        return True
