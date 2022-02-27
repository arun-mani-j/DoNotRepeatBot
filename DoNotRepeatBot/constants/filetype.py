"""File types associated with a snippet."""

from enum import IntEnum


class FileType(IntEnum):
    """File types associated with a snippet."""

    AUDIO = 10
    DOCUMENT = 20
    NONE = 30
    PHOTO = 40
    STICKER = 50
    VIDEO = 60
    VOICE = 70
