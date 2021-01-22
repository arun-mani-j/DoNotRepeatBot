"""
Contains Database object that manages connection to database.
"""

import psycopg2
from .query import Query


class Database:

    """
    Creates a connection to the database.
    The connection is closed automatically when the object is deleted.
    """

    def __init__(self, database_url: str):

        """
        Creates a connection to the database.
        The connection is closed automatically when the object is deleted.
        """

        self.connection = psycopg2.connect(dsn=database_url)

    def __del__(self):

        """
        Closes the connection, when the last reference becomes zero.
        """

        self.connection.close()

    def add_snippet(self, chat_id: int, title: str, snippet: str):

        """
        Adds the given snippet to the database for chat under title.
        Returns True if snippet was added, False if it was updated.
        """

        cursor = self.connection.cursor()
        cursor.execute(Query.ADD_SNIPPET, (chat_id, title, snippet, snippet))
        ret = next(cursor, (False,))[0]
        cursor.close()
        self.connection.commit()
        return ret

    def find_snippets(self, chat_id: int, phrase: str, limit: int = 50):

        """
        Yields all snippets by chat matching the given phrase.
        """

        cursor = self.connection.cursor()
        cursor.execute(Query.FIND_SNIPPETS, (chat_id, phrase, limit))
        yield from cursor
        cursor.close()

    def list_snippets(self, chat_id: int):

        """
        Yields all the titles of snippets by chat.
        """

        cursor = self.connection.cursor()
        cursor.execute(Query.LIST_SNIPPETS, (chat_id,))
        yield from cursor
        cursor.close()

    def remove_snippet(self, chat_id: int, title: str):

        """
        Removes the snippet of given title for chat. Returns True if any snippet was removed.
        """

        cursor = self.connection.cursor()
        cursor.execute(Query.REMOVE_SNIPPET, (chat_id, title))
        ret = next(cursor, (False,))[0]
        cursor.close()
        self.connection.commit()
        return ret

    def update_snippet_usage(self, chat_id: int, title: str):

        """
        Increments the snippet usage by one.
        """

        cursor = self.connection.cursor()
        cursor.execute(Query.UPDATE_USAGE, (chat_id, title))
        cursor.close()
        self.connection.commit()
