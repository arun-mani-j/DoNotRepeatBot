"""Handlers for inline queries."""

from telegram import Update, InlineQueryResultsButton
from telegram.ext import CallbackContext

from DoNotRepeatBot.constants import Literal


async def increment(update: Update, context: CallbackContext):
    """Increment the popularity of a snippet."""

    if update.chosen_inline_result is None:
        raise RuntimeError()

    database = context.bot_data["database"]
    title = update.chosen_inline_result.result_id
    chat_id = update.chosen_inline_result.from_user.id
    database.increment_snippet_usage(chat_id, title)


async def search(update: Update, context: CallbackContext):
    """Answer an inline query to search snippet."""

    if update.inline_query is None:
        raise RuntimeError()

    database = context.bot_data["database"]
    gettext = context.bot_data["gettext"]
    inl_qry = update.inline_query
    query = inl_qry.query[: Literal.MAX_TITLE_LENGTH]
    snippets = database.search_snippets(
        inl_qry.from_user.id, query, Literal.MAX_RESULTS_SIZE
    )
    results = [snip.to_inline_result() for snip in snippets]
    await inl_qry.answer(
        results=results,
        is_personal=True,
        cache_time=Literal.CACHE_TIME,
        button=InlineQueryResultsButton(
            text=gettext.SWITCH_PM, start_parameter=Literal.PAYLOAD_ADD
        ),
    )
