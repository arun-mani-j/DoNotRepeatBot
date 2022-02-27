"""
Contains Query object with query strings.
"""


class Query:
    """
    Query has queries for various purposes that are used by the database connector.
    """

    ADD_CHAT = (
        "INSERT INTO chats "
        "VALUES (%(chat_id)s, %(lang)s) "
        "ON CONFLICT (chat_id) DO NOTHING;"
    )

    ADD_SNIPPET = (
        "INSERT INTO snippets "
        "VALUES (DEFAULT, %(chat_id)s, %(title)s, %(body)s, "
        "%(file_id)s, %(file_type)s, DEFAULT, DEFAULT) "
        "ON CONFLICT (chat_id, title) DO UPDATE "
        "SET body=%(body)s, file_id=%(file_id)s, file_type=%(file_type)s "
    )

    CLEAR_SNIPPETS = "DELETE FROM snippets WHERE chat_id = %(chat_id)s;"

    DELETE_SNIPPET = (
        "DELETE FROM snippets "
        "WHERE chat_id = %(chat_id)s AND title = %(title)s "
        "RETURNING TRUE;"
    )

    GET_LANGUAGE = "SELECT lang FROM chats WHERE chat_id = %(chat_id)s;"

    GET_SNIPPET_BY_ID = (
        "SELECT chat_id, title, body, file_id, file_type FROM snippets "
        "WHERE snippet_id = %(snippet_id)s;"
    )

    GET_SNIPPET_BY_TITLE = (
        "SELECT chat_id, title, body, file_id, file_type FROM snippets "
        "WHERE chat_id = %(chat_id)s AND title = %(title)s;"
    )

    GET_SNIPPETS_COUNT = (
        "SELECT count(title) FROM snippets WHERE chat_id = %(chat_id)s;"
    )

    INCREMENT_USAGE = (
        "UPDATE snippets SET usage = usage + 1 "
        "WHERE chat_id = %(chat_id)s AND title = %(title)s;"
    )

    LIST_SNIPPETS = (
        "SELECT snippet_id, title FROM snippets WHERE chat_id = %(chat_id)s;"
    )

    SEARCH_SNIPPETS = (
        "SELECT chat_id, title, body, file_id, file_type FROM snippets "
        "WHERE chat_id = %(chat_id)s AND "
        "(vectorized @@ PLAINTO_TSQUERY(%(query)s) OR "
        "COALESCE(title, '') || ' ' || COALESCE(body, '') "
        "ILIKE '%%' || %(query)s || '%%') "
        "ORDER BY usage DESC LIMIT %(limit)s;"
    )

    SET_LANGUAGE = "UPDATE chats SET lang = %(lang)s WHERE chat_id = %(chat_id)s;"
