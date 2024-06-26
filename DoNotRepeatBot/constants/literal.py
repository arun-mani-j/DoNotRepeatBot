"""Constants of primary data type and literals."""

import os

from telegram.constants import InlineQueryLimit, MessageLimit, UpdateType


class Literal:
    """Constants of primary data type and literals."""

    CACHE_TIME = 0

    DEFAULT_LANG = "en"

    MAX_BODY_LENGTH = int(0.99 * MessageLimit.MAX_TEXT_LENGTH)

    # Inline results ID is limited to 64 bytes and we take 4 bytes for custom usage.
    MAX_TITLE_LENGTH = 60

    MAX_LIST_SIZE = (MAX_BODY_LENGTH // MAX_TITLE_LENGTH) - 1

    PAYLOAD_ADD = "ADD"

    PAYLOAD_ID = "ID"

    PAYLOADS = (PAYLOAD_ADD, PAYLOAD_ID)

    TRANSLATIONS = [
        dr for dr in os.listdir("locales") if os.path.isdir(f"locales/{dr}")
    ]

    UPDATES = [
        UpdateType.CHOSEN_INLINE_RESULT,
        UpdateType.INLINE_QUERY,
        UpdateType.MESSAGE,
        UpdateType.MY_CHAT_MEMBER,
    ]

    MAX_RESULTS_SIZE = InlineQueryLimit.RESULTS
