"""Constants of primary data type and literals."""

import os

from telegram.constants import (MAX_INLINE_QUERY_RESULTS, MAX_MESSAGE_LENGTH,
                                UPDATE_CHOSEN_INLINE_RESULT,
                                UPDATE_INLINE_QUERY, UPDATE_MESSAGE,
                                UPDATE_MY_CHAT_MEMBER)


class Literal:
    """Constants of primary data type and literals."""

    CACHE_TIME = 0

    DEFAULT_LANG = "en"

    MAX_BODY_LENGTH = int(0.99 * MAX_MESSAGE_LENGTH)

    # Inline results id is limited to 64 bytes and we take 4 bytes for custom usage.
    MAX_TITLE_LENGTH = 60

    MAX_LIST_SIZE = (MAX_BODY_LENGTH // MAX_TITLE_LENGTH) - 1

    PAYLOAD_ADD = "ADD"

    PAYLOAD_ID = "ID"

    PAYLOADS = (PAYLOAD_ADD, PAYLOAD_ID)

    TRANSLATIONS = [
        dr for dr in os.listdir("locales") if os.path.isdir(f"locales/{dr}")
    ]

    UPDATES = [
        UPDATE_CHOSEN_INLINE_RESULT,
        UPDATE_INLINE_QUERY,
        UPDATE_MESSAGE,
        UPDATE_MY_CHAT_MEMBER,
    ]

    MAX_RESULTS_SIZE = MAX_INLINE_QUERY_RESULTS
