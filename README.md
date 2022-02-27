# Introduction

Sometimes in some point of life, you may think that a lot of messages, a lot of times are just repeating.
From _Hii_, _How are you_, _What's up ?_ to _Thank you_, _Good night_.
Yes these are small, but there are also other huge messages that we have to sit and type every time!

Stop repeating yourself! Just [Do Not Repeat Yourself](https://en.wikipedia.org/wiki/Don't_repeat_yourself).

# DoNotRepeatBot

[DoNotRepeatBot](https://t.me/DoNotRepeatBot) is a Telegram bot that saves messages for you, so you can send them in any chat with just a few key presses.
All your snippets are stored in the bot's database and can be accessed and updated easily.

# Getting Started

Open [DoNotRepeatBot](https://t.me/DoNotRepeatBot) in Telegram and send it a `/guide` command.

# Documentation

Documentation about the commands, usage etc. is available under `/help` command.

# Development

The bot's source code is under GPL v3 license. Feel free to fork the repository and make changes as you wish.
If you have any improvements, bug reports, feature requests, please open a new issue or ask in [DoNotRepeatBot Group](https://t.me/donotrepeat).

# Translation

The translation related files are located under [/locales](/locales). Familiarity with (GNU gettext)[https://www.gnu.org/software/gettext] will help you a lot.
Please add or improve existing translation and create a [pull request](/pulls).

# Self Hosting

Hosting the bot yourself is dead easy. Have some patience and a good internet connection.

## Requirements

The following applications / modules are important for running the bot.

1. [Python](https://python.org)
   Python is the programming language in which the bot is written.
2. [Python Telegram Bot](https://python-telegram-bot.org)
   This package is necessary to interact with Telegram.
3. [PostgreSQL](https://www,postgresql.org)
   PostgreSQL is a relational database management system. It is used to store snippets.
4. [psycopg](https://psycopg.org)
   This package allows connecting to database using Python.

All the above requirements are free and open-source. You can download and install them for free.

## Grabbing The Source Code

Next step is downloading a copy of the bot. This can be done by cloning the repository (via `git`) or Github website's features.
After downloading, move the directory to a convenient location.

## Setting Up Database

After installing database, you need to set up tables. Open a Terminal or Console in the bot's directory and enter the following command.

```psql
$ psql -f data/schema.sql
```

## Initializing The Bot

Go to [BotFather](https://t.me/BotFather) and get a bot token.
Following this, make your [database URL](https://stackoverflow.com/questions/3582552/postgresql-connection-url).
Then, export the values as your [environment variables](https://en.wikipedia.org/wiki/Environment_variable). For example in a UNIX shell, you can do.

```bash
$ export TOKEN="<TOKEN>"
$ export DATABASE_URL="<DATABASE URL>"
```

## Starting The Bot

Congrats, now you are on the final steps! Based on the capabilities of your server (the computer), you can use the following ways.
Depending on the environment variables, the bot automatically uses polling or webhooks.

### Polling

Polling asks Telegram server periodically for updates and handles them. To start the bot in polling method, open a Terminal or Console in the bot's directory and execute the following command.

```bash
$ python3 -m DoNotRepeatBot
```

Here `python3` is name of Python interpreter in your system. Based on your operating system, it can be `py3`, `python` or something else.
If you had changed the directory names, that is if you are using some other name instead of `DoNotRepeatBot`, use that name.

You can changed the polling interval using `INTERVAL` (should be an integer) environment variable.

### Webhooks

Webhooks work on a different method. Here Telegram sends you updates as they are received. Setting up webhooks can be irritating but they worth the pain.
Beforing diving deep, read the following articles. They can clear most of the doubts and how-tos.

1. [Where to host Telegram Bots](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Where-to-host-Telegram-Bots)
2. [How to host your bot](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Hosting-your-bot)
3. [Webhooks](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks)

After reading the above, export the following environment variables.

1. `LISTEN` - the URL on which the bot listens.
2. `URL` - The URL to which Telegram sends updates.
3. `PORT` - The port on which the bot listens.

Note that both 1 and 2 are URLs and don't append any extra _slash_ at the end of URL. That is, your link should be `https://www.example.com` and not `https://www.example.com/`.
The value of port should be an integer.

Now start your bot with the following command, as did in polling.

```
$ python3 -m DoNotRepeatBot
```

## Done

Everything should work fine now! Check it and if you have any doubt, please ask in [DoNotRepeatBot Group](https://t.me/donotrepeat).
