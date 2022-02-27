"""Interface to database."""

import psycopg

from DoNotRepeatBot.constants import Query

from .snippet import Snippet


def _next(cur: psycopg.Cursor, default=None):
    """Get the next row of cursor else default."""
    row = cur.fetchone()
    return row if row else default


class Database:
    """Interface to database."""

    def __init__(self, database_url: str):
        """Interface to database."""
        self.cnx = psycopg.connect(database_url)

    def _failsafe(func):
        """Commit or rollback facility for queries."""

        def wrapped(self, *args, **kwargs):
            try:
                ret = func(self, *args, **kwargs)
            except psycopg.Error as e:
                self.cnx.rollback()
                raise e
            else:
                self.cnx.commit()
                return ret

        return wrapped

    @_failsafe
    def add_chat(self, chat_id: int, lang: str):
        """Insert a chat to chats table."""
        cur = self.cnx.cursor()
        cur.execute(Query.ADD_CHAT, {"chat_id": chat_id, "lang": lang})
        cur.close()

    @_failsafe
    def add_snippet(self, snippet: Snippet):
        """Insert or update a snippet."""
        cur = self.cnx.cursor()
        cur.execute(Query.ADD_SNIPPET, snippet.to_dict())
        cur.close()

    @_failsafe
    def clear_snippets(self, chat_id: int):
        """Clear snippets of a chat."""
        cur = self.cnx.cursor()
        cur.execute(Query.CLEAR_SNIPPETS, {"chat_id": chat_id})
        cur.close()

    @_failsafe
    def delete_snippet(self, chat_id: int, title: str) -> bool:
        """Delete a snippet.
        Return True if deleted, False on otherwise."""
        cur = self.cnx.cursor()
        cur.execute(Query.DELETE_SNIPPET, {"chat_id": chat_id, "title": title})
        (deleted,) = _next(cur, (False,))
        cur.close()
        return deleted

    def get_language(self, chat_id: int) -> str:
        """Get the language for a chat."""
        cur = self.cnx.cursor()
        cur.execute(Query.GET_LANGUAGE, {"chat_id": chat_id})
        (lang,) = _next(cur, (None,))
        cur.close()
        return lang

    def get_snippet_by_id(self, snippet_id: str) -> Snippet:
        """Get the snippet with the ID."""
        cur = self.cnx.cursor()
        cur.execute(Query.GET_SNIPPET_BY_ID, {"snippet_id": snippet_id})
        params = _next(cur, ())
        if params:
            snippet = Snippet(*params)
        else:
            snippet = None
        cur.close()
        return snippet

    def get_snippet_by_title(self, chat_id: int, title: str) -> Snippet:
        """Get the snippet of the chat with the title."""
        cur = self.cnx.cursor()
        cur.execute(Query.GET_SNIPPET_BY_TITLE, {"chat_id": chat_id, "title": title})
        params = _next(cur, ())
        if params:
            snippet = Snippet(*params)
        else:
            snippet = None
        cur.close()
        return snippet

    def get_snippets_count(self, chat_id: int) -> (int, str):
        """Get snippets count and language for a chat."""
        cur = self.cnx.cursor()
        cur.execute(Query.GET_SNIPPETS_COUNT, {"chat_id": chat_id})
        (count,) = _next(cur, (0,))
        cur.close()
        return count

    @_failsafe
    def increment_snippet_usage(self, chat_id: int, title: str):
        """Increment the usage of a snippet."""
        cur = self.cnx.cursor()
        cur.execute(Query.INCREMENT_USAGE, {"chat_id": chat_id, "title": title})
        cur.close()

    def list_snippets(self, chat_id: int) -> list:
        """Yield snippet titles and their ID for a chat."""
        cur = self.cnx.cursor()
        cur.execute(Query.LIST_SNIPPETS, {"chat_id": chat_id})
        snips = cur.fetchall()
        cur.close()
        return snips

    def search_snippets(self, chat_id: int, query: str, limit: int):
        """Search snippets matching given query."""
        cur = self.cnx.cursor()
        cur.execute(
            Query.SEARCH_SNIPPETS,
            {"chat_id": chat_id, "query": query, "limit": limit},
        )
        for row in cur:
            yield Snippet(*row)
        cur.close()

    @_failsafe
    def set_language(self, chat_id: int, lang: str):
        """Set language for a chat."""
        cur = self.cnx.cursor()
        cur.execute(Query.SET_LANGUAGE, {"chat_id": chat_id, "lang": lang})
        cur.close()
