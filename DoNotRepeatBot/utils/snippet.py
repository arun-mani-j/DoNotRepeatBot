"""Snippet and its related functions."""

from dataclasses import asdict, dataclass, field

from telegram import (InlineQueryResultArticle, InlineQueryResultCachedAudio,
                      InlineQueryResultCachedDocument,
                      InlineQueryResultCachedPhoto,
                      InlineQueryResultCachedSticker,
                      InlineQueryResultCachedVideo,
                      InlineQueryResultCachedVoice, InputTextMessageContent)
from telegram import Message as TgMessage

from DoNotRepeatBot.constants import FileType, Literal, Message


@dataclass
class Snippet:
    """Snippet for easy snippet operations."""

    chat_id: int
    title: str
    body: str
    file_id: str
    file_type: field(default_factory=FileType)

    def from_message(message: TgMessage, title: str = None):
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
        kwargs = {
            "id": self.title,
            "title": self.title,
            "description": self.body,
            "caption": self.body,
        }
        f_id = self.file_id

        if self.file_type == FileType.AUDIO:
            res = InlineQueryResultCachedAudio(audio_file_id=f_id, **kwargs)
        elif self.file_type == FileType.DOCUMENT:
            res = InlineQueryResultCachedDocument(document_file_id=f_id, **kwargs)
        elif self.file_type == FileType.PHOTO:
            res = InlineQueryResultCachedPhoto(photo_file_id=f_id, **kwargs)
        elif self.file_type == FileType.STICKER:
            res = InlineQueryResultCachedSticker(sticker_file_id=f_id, **kwargs)
            del kwargs["caption"]
        elif self.file_type == FileType.VIDEO:
            res = InlineQueryResultCachedVideo(video_file_id=f_id, **kwargs)
        elif self.file_type == FileType.VOICE:
            res = InlineQueryResultCachedVoice(voice_file_id=f_id, **kwargs)
        else:
            msg_cnt = InputTextMessageContent(self.body)
            del kwargs["caption"]
            res = InlineQueryResultArticle(input_message_content=msg_cnt, **kwargs)

        return res

    def to_sendable(self, message: Message):
        """Convert self to return a function and kwargs \
        that replies the snippet to given message."""
        kwargs = {"caption": self.body}
        func = None

        if self.file_type == FileType.AUDIO:
            kwargs["audio"] = self.file_id
            func = message.reply_audio
        elif self.file_type == FileType.DOCUMENT:
            kwargs["document"] = self.file_id
            func = message.reply_document
        elif self.file_type == FileType.PHOTO:
            kwargs["photo"] = self.file_id
            func = message.reply_photo
        elif self.file_type == FileType.STICKER:
            kwargs["sticker"] = self.file_id
            func = message.reply_sticker
            del kwargs["caption"]
        elif self.file_type == FileType.VIDEO:
            kwargs["video"] = self.file_id
            func = message.reply_video
        elif self.file_type == FileType.VOICE:
            kwargs["voice"] = self.file_id
            func = message.reply_voice
        else:
            kwargs["text"] = self.body
            func = message.reply_text
            del kwargs["caption"]

        return func, kwargs
