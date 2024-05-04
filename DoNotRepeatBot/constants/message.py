"""Contains Message object which is used for interacting with users.
All interactions can be changed from here without \
messing up in source code."""

import gettext

_ = gettext.gettext


class Message:
    """Message has all form of outgoing messages from the bot. \
    It is contained in a separate object for easy updations and deletions."""

    ADDED_SNIPPET = _("<code>{TITLE}</code> has been added successfully.")

    CLEARED_SNIPPETS = _("All the snippets have been cleared!")

    DELETED_SNIPPET = _("<code>{TITLE}</code> has been deleted.")

    GUIDE = _(
        "@DoNotRepeatBot is a bot to share messages at multiple places when needed "
        "without the need to create the message again.\n\n"
        "Take it like this. You have a message you happen to use at multiple chats "
        "so what you do is, save the message to <i>Saved Messages</i> and forward "
        "it everytime you need it.\n"
        "@DoNotRepeatBot does the same, but with extra features and more streamlined!\n\n"
        "<b>Getting Started</b>\n"
        "Let's start with a simple example. Start the bot in private message. "
        "Type and send <code>/add hello</code>.\n"
        "Now the bot will ask you for the message to store. Simply send a "
        "textual message. It can be anything of your creativity!\n\n"
        "The bot should say that the snippet has been added.\n\n"
        "Next, type @DoNotRepeatBot, press <code>space</code> and type <i>hello</i>.\n"
        "The bot should suggest you the snippet you added, tap on it and the bot sends "
        "it to the chat! That's it!\n\n"
        "If you don't get the snippet, make sure you are typing the title correctly. "
        "Else, try after a few seconds, as Telegram might <i>cache</i> the results.\n"
        "What we saw now is just a tip of the features, the bot can do!\n\n"
        "You can learn more about the bot from the "
        "<a href='https://github.com/j-arun-mani/DoNotRepeatBot'>repository</a>.\n"
        "There is also /help to give you overview of available commands and methods.\n"
        "Finally, feel free to tell your thoughts and feedback in @DoNotRepeat 😉!"
    )

    HELP = _(
        "If you are very new to me, you might wanna check /guide first 😁\n\n"
        "<b>Syntax</b>\n"
        "• <code>[ARG]</code> - <code>ARG</code> is optional and "
        "need not be provided.\n"
        "• <code>&lt;ARG&gt;</code> - <code>ARG</code> is essential and "
        "must be provided.\n\n"
        "<b>Commands</b>\n"
        "• /add <code>[title]</code>\n"
        "This command creates a new snippet with title provided.\n"
        "If title is not provided, then the first few characters of the snippet "
        "body is used a title. If used as it is, I will prompt you for snippet. "
        "If the command is a reply to a message, then that message is used.\n"
        "A message to be made snippet can be normal message or file "
        "(audio, photo, video etc.) or a sticker. Title is mandatory if the message "
        "doesn't have any textual content.\n\n"
        "• /clear\n"
        "Clear all the snippets of the chat.\n"
        "Be careful before using it!\n\n"
        "• /del <code>&lt;title&gt;</code>\n"
        "Delete the snippet with given title.\n\n"
        "• /done\n"
        "Finish import of snippets.\n\n"
        "• /get <code>&lt;title&gt;</code>\n"
        "Get the snippet of given title.\n"
        "Equivalent to <code>#title</code> or inline mode.\n\n"
        "• /guide\n"
        "Present a beginner friendly tutorial.\n\n"
        "• /help\n"
        "The very same help message.\n\n"
        "• /import\n"
        "Start the import process.\n"
        "Using <i>import</i>, you can add multiple snippets without invidual /add.\n"
        "First send /import and send (or forward) messages to added. "
        "The title is automatically obtained from first few characters of the textual "
        "content. Use /done to finish the import.\n\n"
        "• /lang <code>[lang]</code>\n"
        "Change my language to <code>lang</code>.\n"
        "Send the command without any language to view available languages.\n\n"
        "• /list\n"
        "List the snippets associated with the chat.\n"
        "Tap the title to view the snippet.\n\n"
        "• /start\n"
        "Start the adventure.\n\n"
        "<b>Inline Mode</b>\n"
        "Type @DoNotRepeatBot in a chat and press space.\n"
        "I will show you available snippets which you can filter by typing title or "
        "text of the snippet.\n\n"
        "<b>Text</b>\n"
        "Use #hashtag notation to get snippets via title.\n"
        "For example, #hello will send snippet named <code>hello</code>\n\n"
        "<b>Notes</b>\n"
        "1. Addition, deletion and other manipulation tasks require the user to be "
        "an admin in groups.\n"
        "2. Language is automatically set to the language the user uses. For groups "
        "it is always set to English unless changed by an admin.\n\n"
        "You can learn more about me from the "
        "<a href='https://github.com/j-arun-mani/DoNotRepeatBot'>repository</a>.\n"
        "There is also /help to give you overview of available commands and methods.\n"
        "Finally, feel free to tell your thoughts and feedback in @DoNotRepeat 😉!"
    )

    IMPORT_DONE = _(
        "<b>Import Completed</b>\n"
        "• Total messages : <code>{TOTAL}</code>\n"
        "• Imported snippets : <code>{IMPORTED}</code>\n"
        "• Failed to import : <code>{FAILED}</code>"
    )

    IMPORT_STARTED = _(
        "Mass send me the messages to be added as snippets. "
        "Use /done to signal finish."
    )

    INVALID_MESSAGE = _("The command should be a reply to a valid message.")

    INVALID_PERMISSIONS = _("You are not allowed to perform this action.")

    INVALID_START = _("That's not how you start me … Need some /help?")

    LANGUAGES = _(
        "Available languages are {LANGS}.\n"
        "Can't find your language? "
        "Please help us at @DoNotRepeat to translate the bot to your language."
    )

    LIST_ITEM = _("• <a href='{LINK}?start={ID}{LOAD}'>{TITLE}</a>")

    MISSING_BODY = _("A snippet can't be made out of that message.")

    MISSING_TITLE = _(
        "Title is required! Either mention it directly "
        "or the message you replied to should have a textual content."
    )

    NO_SNIPPETS = _("There are no snippets associated with this chat.")

    SEND_SNIPPET = _("Send me the snippet to add.")

    SET_LANGUAGE = _("Language has been set to <code>{LANG}</code>.")

    SNIPPET_NOT_FOUND = _(
        "<code>{TITLE}</code> not found. Use /list to view all your snippets."
    )

    START = _(
        "Hey there!\n"
        "I'm @DoNotRepeatBot. "
        "Never ever repeat the hassle of sending same message again! "
        "Please check /help for more information."
    )

    STATS = _(
        "• Chat ID : <code>{CHAT_ID}</code>\n"
        "• Snippets : <code>{COUNT}</code>\n"
        "• Language : <code>{LANG}</code>"
    )

    SWITCH_PM = _("Create a new snippet")

    UNKNOWN_ERROR = _(
        "Something went wrong. Yes, I won't tell you what happened though."
    )
