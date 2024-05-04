"""GetText interface for translated strings."""

import gettext

from DoNotRepeatBot.constants import Literal, Message


class GetText:
    """GetText interface for translated strings."""

    def __init__(self, lang: str = Literal.DEFAULT_LANG):
        """GetText interface for translated strings."""
        self.lang = ""
        self.translator = gettext.NullTranslations()
        gettext.find("message", "locales", Literal.TRANSLATIONS, True)
        self.set_language(lang)

    def __getattr__(self, name: str) -> str:
        """Return translated message by attribute name."""
        text = getattr(Message, name)
        return self.get(text)

    def get(self, text: str) -> str:
        """Return translated message of given text."""
        return self.translator.gettext(text)

    def set_language(self, lang: str):
        """Set language of the translator."""
        if self.lang == lang:
            return
        self.lang = lang
        self.translator = gettext.translation("message", "locales", [self.lang])
