"""Commands available to bot."""

from telegram import (BotCommandScopeAllChatAdministrators,
                      BotCommandScopeAllGroupChats,
                      BotCommandScopeAllPrivateChats)

admin = [
    ("add", "Add a snippet"),
    ("clear", "Clear ALL snippets"),
    ("del", "Delete a snippet"),
    ("done", "Marks import as done"),
    ("import", "Import snippets"),
    ("lang", "Language of interaction"),
]

member = [
    ("get", "Get a snippet"),
    ("guide", "Getting started guide"),
    ("help", "Help on usage"),
    ("list", "List available snippets"),
    ("start", "Start the adventure"),
    ("stats", "Statistics to bore you"),
]

commands = {
    BotCommandScopeAllChatAdministrators(): admin + member,
    BotCommandScopeAllGroupChats(): member,
    BotCommandScopeAllPrivateChats(): admin + member,
}
