"""Handlers for inline queries."""

from telegram import Update
from telegram.ext import CallbackContext

from DoNotRepeatBot.constants import Literal


def increment(update: Update, context: CallbackContext):
    """Increment the popularity of a snippet."""
    database = context.bot_data["database"]
    title = update.chosen_inline_result.result_id
    chat_id = update.chosen_inline_result.from_user.id
    database.increment_snippet_usage(chat_id, title)


def search(update: Update, context: CallbackContext):
    """Answer an inline query to search snippet."""
    database = context.bot_data["database"]
    gettext = context.bot_data["gettext"]
    inl_qry = update.inline_query
    query = inl_qry.query[: Literal.MAX_TITLE_LENGTH]
    snippets = database.search_snippets(
        inl_qry.from_user.id, query, Literal.MAX_RESULTS_SIZE
    )
    results = [snip.to_inline_result() for snip in snippets]
    inl_qry.answer(
        results=results,
        is_personal=True,
        cache_time=Literal.CACHE_TIME,
        switch_pm_text=gettext.SWITCH_PM,
        switch_pm_parameter=Literal.PAYLOAD_ADD,
    )
