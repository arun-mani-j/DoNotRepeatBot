"""
Functions used for specific operations.
"""

from telegram import InlineQueryResultArticle, InputTextMessageContent


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


def get_results(database, user_id, keyword):

    """
    Gets results specific to user and matching given keyword.
    """

    results = []

    for title, snippet in database.find_snippets(user_id):
        if keyword not in title:
            continue
        content = InputTextMessageContent(message_text=snippet, parse_mode="HTML")
        article = InlineQueryResultArticle(
            id=title[:64],
            title=title,
            input_message_content=content,
            description=snippet,
        )
        results.append(article)

    return results
