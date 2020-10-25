"""
Contains Query object with query strings.
"""


class Query:
    """
    Query has queries for various purposes that are used by the database connector.
    """

    ADD_SNIPPET = (
        "INSERT INTO snippets(user_id, title, snippet) VALUES (%s, %s, %s) "
        "ON CONFLICT (user_id, title) DO UPDATE SET snippet = %s RETURNING TRUE;"
    )

    COMMON_SNIPPETS = "SELECT title, snippet FROM common_snippets LIMIT %s;"

    FIND_SNIPPETS = (
        "SELECT title, snippet FROM snippets "
        "WHERE user_id = %s AND title @@ %s LIMIT %s;"
    )

    LIST_SNIPPETS = "SELECT title FROM snippets WHERE user_id = %s;"

    REMOVE_SNIPPET = (
        "DELETE FROM snippets WHERE user_id = %s AND title = %s RETURNING TRUE;"
    )
