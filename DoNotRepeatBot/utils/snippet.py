"""Snippet and its related functions."""

from dataclasses import asdict, dataclass
from typing import Callable

from telegram import (
    InlineQueryResultArticle,
    InlineQueryResultCachedAudio,
    InlineQueryResultCachedDocument,
    InlineQueryResultCachedPhoto,
    InlineQueryResultCachedSticker,
    InlineQueryResultCachedVideo,
    InlineQueryResultCachedVoice,
    InputTextMessageContent,
)
from telegram import Message as TMessage

from DoNotRepeatBot.constants import FileType, Literal, Message


def _simplify(text: str) -> str:
    return "".join(c for c in text if c.isalnum())


@dataclass
class Snippet:
    """Snippet for easy snippet operations."""

    chat_id: int
    title: str
    body: str
    file_id: str | None
    file_type: FileType = FileType.NONE

    @staticmethod
    def from_message(message: TMessage, title: str | None = None):
        """Create a snippet from message.
        Title is automatically parsed from message if not provided."""
        if message is None:
            raise ValueError(Message.INVALID_MESSAGE)

        chat_id = message.chat.id
        body = message.caption or message.text
        title = title or body

        if not (title and title.strip()):
            raise ValueError(Message.MISSING_TITLE)
        title = title[: Literal.MAX_TITLE_LENGTH].strip()

        if message.caption:
            body = message.caption_html_urled
        else:
            body = message.text_html_urled

        if message.audio:
            file_id = message.audio.file_id
            file_type = FileType.AUDIO
        elif message.document:
            file_id = message.document.file_id
            file_type = FileType.DOCUMENT
        elif message.photo:
            file_id = message.photo[-1].file_id
            file_type = FileType.PHOTO
        elif message.sticker:
            file_id = message.sticker.file_id
            file_type = FileType.STICKER
        elif message.video:
            file_id = message.video.file_id
            file_type = FileType.VIDEO
        elif message.voice:
            file_id = message.voice.file_id
            file_type = FileType.VOICE
        else:
            file_id = None
            file_type = FileType.NONE

        if not (body or file_id):
            raise ValueError(Message.MISSING_BODY)

        return Snippet(chat_id, title, body, file_id, file_type)

    def to_dict(self):
        """Convert self to a dict."""
        return asdict(self)

    def to_inline_result(self):
        """Convert self to an inline result."""
        id_ = _simplify(self.title)
        file_id = self.file_id

        if self.file_type == FileType.AUDIO:
            res = InlineQueryResultCachedAudio(
                id=id_, title=self.title, audio_file_id=file_id, caption=self.body
            )
        elif self.file_type == FileType.DOCUMENT:
            res = InlineQueryResultCachedDocument(
                id=id_, title=self.title, document_file_id=file_id, caption=self.body
            )
        elif self.file_type == FileType.PHOTO:
            res = InlineQueryResultCachedPhoto(
                id=id_, title=self.title, photo_file_id=file_id, caption=self.body
            )
        elif self.file_type == FileType.STICKER:
            res = InlineQueryResultCachedSticker(id=id_, sticker_file_id=file_id)
        elif self.file_type == FileType.VIDEO:
            res = InlineQueryResultCachedVideo(
                id=id_, title=self.title, video_file_id=file_id, caption=self.body
            )
        elif self.file_type == FileType.VOICE:
            res = InlineQueryResultCachedVoice(
                id=id_,
                title=self.title,
                voice_file_id=file_id,
            )
        else:
            content = InputTextMessageContent(self.body)
            res = InlineQueryResultArticle(
                id=id_,
                title=self.title,
                input_message_content=content,
            )

        return res

    def to_sendable(self, message: TMessage) -> tuple[Callable, dict]:
        """Convert self to return a function and kwargs \
        that replies the snippet to given message."""
        kwargs = {"caption": self.body}
        func: Callable

        if self.file_id and self.file_type == FileType.AUDIO:
            kwargs["audio"] = self.file_id
            func = message.reply_audio
        elif self.file_id and self.file_type == FileType.DOCUMENT:
            kwargs["document"] = self.file_id
            func = message.reply_document
        elif self.file_id and self.file_type == FileType.PHOTO:
            kwargs["photo"] = self.file_id
            func = message.reply_photo
        elif self.file_id and self.file_type == FileType.STICKER:
            kwargs["sticker"] = self.file_id
            func = message.reply_sticker
            del kwargs["caption"]
        elif self.file_id and self.file_type == FileType.VIDEO:
            kwargs["video"] = self.file_id
            func = message.reply_video
        elif self.file_id and self.file_type == FileType.VOICE:
            kwargs["voice"] = self.file_id
            func = message.reply_voice
        else:
            kwargs["text"] = self.body
            func = message.reply_text
            del kwargs["caption"]

        return func, kwargs
