"""
Contains Query object with query strings.
"""


class Query:
    """
    Query has queries for various purposes that are used by the database connector.
    """

    ADD_SNIPPET = (
        "INSERT INTO snippets(chat_id, title, snippet) VALUES (%s, %s, %s) "
        "ON CONFLICT (chat_id, title) "
        "DO UPDATE SET snippet = %s RETURNING TRUE;"
    )

    FIND_SNIPPETS = (
        "SELECT title, snippet FROM snippets "
        "WHERE chat_id = %s AND title ILIKE '%%' || %s || '%%' "
        "ORDER BY usage DESC LIMIT %s;"
    )

    LIST_SNIPPETS = "SELECT title FROM snippets WHERE chat_id = %s;"

    REMOVE_SNIPPET = (
        "DELETE FROM snippets " "WHERE chat_id = %s AND title = %s RETURNING TRUE;"
    )

    UPDATE_USAGE = (
        "UPDATE snippets SET usage = usage + 1 WHERE chat_id = %s AND title = %s;"
    )
