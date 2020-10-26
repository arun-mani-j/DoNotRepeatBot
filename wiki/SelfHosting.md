# Self Hosting
 Hosting the bot yourself is dead easy. Have some patience and a good internet connection.

## Requirements
 The following applications / modules are important for running the bot. 
 
 1. [Python](https://python.org)
   Python is a programming language in which the bot is written.
 2. [Python Telegram Bot](https://python-telegram-bot.org)
   This package is necessary to interact with Telegram.
 3. [PostgreSQL](https://www,postgresql.org)
   PostgreSQL is a relational database management system. It is used to store snippets.
 4. [PSYCOPG](https://psycopg.org)
   This package allows connecting to database using Python.
 
 All the above requirements are free and open-source. You can download and install them for free.
 
## Grabbing The Source Code
 Next step is downloading a copy of the bot. This can be done by cloning the repository (via `git`) or Github website's features.
 After downloading, move the directory to a convenient location.
 
## Setting Up Database
 After installing database, you need to set up tables. Open a Terminal or Console in the bot's directory and enter the following command.
 ```
 $ psql -f data/database.sql
 $ psql -f data/commons.sql
 ```
 
## Initializing The Bot
 Go to [BotFather](https://t.me/BotFather) and get a bot token.
 Following this, make your [database URL](https://stackoverflow.com/questions/3582552/postgresql-connection-url).
 
 Then, export the values as your [environment variables](https://en.wikipedia.org/wiki/Environment_variable). For example in a UNIX shell, you can do this :
 ```
 $ export TOKEN="<TOKEN>"
 $ export DATABASE_URL="<DATABASE URL>"
 ```
 
 Note the name of the variables. Use the exact naming as in the example.
 
## Starting The Bot
 Congrats, now you are on the final steps ! Based on the capabilities of your server (the computer), you can use the following ways.
 
### Polling
 Polling asks Telegram server periodically for updates and handles them. To start the bot in polling method, open a Terminal or Console in the bot's directory and execute the following command.
 ```
 $ python3 -m DoNotRepeatBot -p
 ```
 
 Here `python3` is name of Python interpreter in your system. Based on your operating system, it can be `py3`, `python` or something else.
 If you had changed the directory names, that is if you are using some other name instead of `DoNotRepeatBot`, use that name.
 
### Webhooks
 Webhooks work on a different method. Here Telegram sends you updates as they are received. Setting up webhooks can be irritating but they worth the pain.
 Beforing diving deep, read the following articles. They can clear most of the doubts and how-tos.
 1. [Where to host Telegram Bots](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Where-to-host-Telegram-Bots) 
 2. [How to host your bot](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Hosting-your-bot)
 3. [Webhooks](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks)
 
 After reading the above, export the following environment variables.
 1. `LISTEN` - the URL to which the bot listens.
 2. `URL` - The URL to be sent to Telegram.
 3. `PORT` - The port on which the bot listens.
 
 Note that both 1 and 2 are URLs and don't append any extra _slash_ at the end of URL. That is, your link should be `https://www.example.com` and not `https://www.example.com/`.
 The value of port should be an integer.
 
 Now start your bot with the following command, as did in polling.
 ```
 $ python3 -m DoNotRepeatBot
 ```
 
## Done
 Everything should work fine now ! Check it and if you have any doubt, please ask in [Do Not Repeat Bot Group](https://t.me/donotrepeat).
