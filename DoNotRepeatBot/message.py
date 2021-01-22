"""
Contains Message object which is used for interacting with users. \
All interactions can be changed or translated from here without messing up in source code.
"""


class Message:
    """
    Message has all form of outgoing messages from the bot. \
    It is contained in a separate object for easy updations and deletions.
    """

    ADD = (
        "Cool. Now send me the text for snippet. "
        "<code>You</code> <i>can</i> <u>use</u> "
        "<b>markups</b> <a href='www.example.com'>too</a> !"
    )

    ADDED_SNIPPET = "There you go with your <code>{TITLE}</code> snippet !"

    DELETE = "Send me the title of snippet to delete."

    DELETED_NONE = (
        "I couldn't find any snippet for <code>{TITLE}</code>.\n"
        "List your /snippets to see what you got."
    )

    DELETED_SNIPPET = "The <code>{TITLE}</code> is off my track for good."

    EMPTY_SNIPPET = "Snippet can't be empty. Please try again."

    EMPTY_TITLE = (
        "Title can't be empty.\n"
        "Please give the title like below.\n"
        " <code>/add hello</code>"
    )

    HELP = (
        "<b>Essential stuff to know about.</b>\n"
        " I'm a bot who can store a snippet of text for you. "
        " After storing, you can access share the snippet easily across chats.\n\n"
        "<b>Commands</b>\n"
        " ∙ /add <code>{TITLE}</code> - Add a new or update a snippet.\n"
        " ∙ /del <code>{TITLE}</code> - Delete a snippet.\n"
        " ∙ /snippets - Lists your snippets.\n\n"
        "<b>Accessing Snippets</b>\n"
        " 1. Go to a chat, type <code>@donotrepeatbot {TITLE}</code>, "
        "where <code>{TITLE}</code> is the name of the snippet."
        " 2. Select the snippet from the list of available options.\n"
        " 3. That's it !\n\n"
        "<b>Usage In Groups</b>\n"
        " 1. Sharing snippets in group is more or less done in the same way.\n"
        " 2. Add the bot to group, and make and remove snippets using commands specified above.\n"
        " 3. Use hashtag notation to access snippets, like <code>#hello</code>, "
        "to access snippet of title <code>hello</code>.\n"
        " 4. Only admins can add and delete snippets, but everyone can access the snippets.\n"
        " 5. If the bot has enough permissions, it will delete the hashtag text too."
        " 6. For hashtags that are reply to another message, the snippet will be shared as its reply.\n\n"
        "<b>Contact The Developers</b>\n"
        " We have a support group : @donotrepeat. "
        "Please ask there for bug reports, questions and feature requests.\n\n"
        "Enjoy !"
    )

    INVALID_PERMISSIONS = "Oops, sorry ! Only admins can add or delete snippets ..."

    NO_RESULTS = "Could not find any snippet matching the title."

    SNIPPET_ITEM = " ∙ <code>{TITLE}</code>"

    SNIPPETS = "These are your snippets.\n{TITLES}"

    START = (
        "Hey there !\n"
        "Never worry more of repeating messages again. "
        "I can help you maintain your text snippets easily.\n\n"
        "Proceed by /add to add a snippet.\n"
        "Look at /help for more information."
    )

    SWITCH_PM = "Add a snippet"

    NO_SNIPPETS = "You don't have any snippets. Why not /add one ?"

    NO_TITLE = "Please specify the title of snippet along with the command."

    UNEXPECTED_MESSAGE = "I don't know what you are talking about ... Need some /help ?"

    UPDATED_SNIPPET = "<code>{TITLE}</code> was updated perfectly."
