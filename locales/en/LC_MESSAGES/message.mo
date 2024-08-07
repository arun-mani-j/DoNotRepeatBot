��          �      �        �   	  1   �  &   �  D     <  F  ,   �  #   �  �   �     U	  �   j	  �	  �	  -   �  N   �       A   (  0   j  1   �  0   �  j   �  +   i  1   �  k   �    3  �   N  1   �  &     D   F  @  �  ,   �  #   �  �        �  �   �  �	  8  -   �(  N   )     c)  A   )  0   �)  1   �)  0   $*  j   U*  +   �*  1   �*  k   +                                                                    
                   	                 <b>Import Completed</b>
• Total messages : <code>{TOTAL}</code>
• Imported snippets : <code>{IMPORTED}</code>
• Failed to import : <code>{FAILED}</code> <code>{TITLE}</code> has been added successfully. <code>{TITLE}</code> has been deleted. <code>{TITLE}</code> not found. Use /list to view all your snippets. @DoNotRepeatBot is a bot to share messages at multiple places when needed without the need to create the message again.

Take it like this. You have a message you happen to use at multiple chats so what you do is, save the message to <i>Saved Messages</i> and forward it everytime you need it.
@DoNotRepeatBot does the same, but with extra features and more streamlined!

<b>Getting Started</b>
Let's start with a simple example. Start the bot in private message. Type and send <code>/add hello</code>.
Now the bot will ask you for the message to store. Simply send a textual message. It can be anything of your creativity!

The bot should say that the snippet has been added.

Next, type @DoNotRepeatBot, press <code>space</code> and type <i>hello</i>.
The bot should suggest you the snippet you added, tap on it and the bot sends it to the chat! That's it!

If you don't get the snippet, make sure you are typing the title correctly. Else, try after a few seconds, as Telegram might <i>cache</i> the results.
What we saw now is just a tip of the features, the bot can do!

You can learn more about the bot from the <a href='https://github.com/j-arun-mani/DoNotRepeatBot'>repository</a>.
There is also /help to give you overview of available commands and methods.
Finally, feel free to tell your thoughts and feedback in @DoNotRepeat 😉! A snippet can't be made out of that message. All the snippets have been cleared! Available languages are {LANGS}.
Can't find your language? Please help us at @DoNotRepeat to translate the bot to your language. Create a new snippet Hey there!
I'm @DoNotRepeatBot. Never ever repeat the hassle of sending same message again! Please check /help for more information. If you are very new to me, you might wanna check /guide first 😁

<b>Syntax</b>
• <code>[ARG]</code> - <code>ARG</code> is optional and need not be provided.
• <code>&lt;ARG&gt;</code> - <code>ARG</code> is essential and must be provided.

<b>Commands</b>
• /add <code>[title]</code>
This command creates a new snippet with title provided.
If title is not provided, then the first few characters of the snippet body is used a title. If used as it is, I will prompt you for snippet. If the command is a reply to a message, then that message is used.
A message to be made snippet can be normal message or file (audio, photo, video etc.) or a sticker. Title is mandatory if the message doesn't have any textual content.

• /clear
Clear all the snippets of the chat.
Be careful before using it!

• /del <code>&lt;title&gt;</code>
Delete the snippet with given title.

• /done
Finish import of snippets.

• /get <code>&lt;title&gt;</code>
Get the snippet of given title.
Equivalent to <code>#title</code> or inline mode.

• /guide
Present a beginner friendly tutorial.

• /help
The very same help message.

• /import
Start the import process.
Using <i>import</i>, you can add multiple snippets without invidual /add.
First send /import and send (or forward) messages to added. The title is automatically obtained from first few characters of the textual content. Use /done to finish the import.

• /lang <code>[lang]</code>
Change my language to <code>lang</code>.
Send the command without any language to view available languages.

• /list
List the snippets associated with the chat.
Tap the title to view the snippet.

• /start
Start the adventure.

<b>Inline Mode</b>
Type @DoNotRepeatBot in a chat and press space.
I will show you available snippets which you can filter by typing title or text of the snippet.

<b>Text</b>
Use #hashtag notation to get snippets via title.
For example, #hello will send snippet named <code>hello</code>

<b>Notes</b>
1. Addition, deletion and other manipulation tasks require the user to be an admin in groups.
2. Language is automatically set to the language the user uses. For groups it is always set to English unless changed by an admin.

You can learn more about me from the <a href='https://github.com/j-arun-mani/DoNotRepeatBot'>repository</a>.
There is also /help to give you overview of available commands and methods.
Finally, feel free to tell your thoughts and feedback in @DoNotRepeat 😉! Language has been set to <code>{LANG}</code>. Mass send me the messages to be added as snippets. Use /done to signal finish. Send me the snippet to add. Something went wrong. Yes, I won't tell you what happened though. That's not how you start me … Need some /help? The command should be a reply to a valid message. There are no snippets associated with this chat. Title is required! Either mention it directly or the message you replied to should have a textual content. You are not allowed to perform this action. • <a href='{LINK}?start={ID}{LOAD}'>{TITLE}</a> • Chat ID : <code>{CHAT_ID}</code>
• Snippets : <code>{COUNT}</code>
• Language : <code>{LANG}</code> Project-Id-Version: 4.0
Report-Msgid-Bugs-To: 
PO-Revision-Date: 2024-05-04 18:20+0530
Last-Translator: Arun Mani J <j.arunmani@proton.me>
Language-Team: English <LL@li.org>
Language: English
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
 <b>Import Completed</b>
• Total messages : <code>{TOTAL}</code>
• Imported snippets : <code>{IMPORTED}</code>
• Failed to import : <code>{FAILED}</code> <code>{TITLE}</code> has been added successfully. <code>{TITLE}</code> has been deleted. <code>{TITLE}</code> not found. Use /list to view all your snippets. @DoNotRepeatBot is a bot to share messages at multiple places when needed without the need to create the message again.
Take it like this. You have a message you happen to use at multiple chats so what you do is, save the message to <i>Saved Messages</i> and forward it everytime you need it.
@DoNotRepeatBot does the same, but with extra features and more streamlined!

<b>Getting Started</b>
Let's start with a simple example. Start the bot in private message. Type and send <code>/add hello</code>.
Now the bot will ask you for the message to store. Simply send a textual message. It can be anything of your creativity!
The bot should say that the snippet has been added.
Next, type @DoNotRepeatBot, press <code>space</code> and type <i>hello</i>.
The bot should suggest you the snippet you added, tap on it and the bot sends it to the chat! That's it!
If you don't get the snippet, make sure you are typing the title correctly. Else, try after a few seconds, as Telegram might <i>cache</i> the results.
What we saw now is just a tip of the features, the bot can do!

You can learn more about the bot by using the <a href='https://github.come/j-arun-mani/DoNotRepeatBot'>documentation</a>.
There is also /help to give you overview of available commands and methods.
Finally, feel free to tell your thoughts and feedback in @DoNotRepeat 😉! A snippet can't be made out of that message. All the snippets have been cleared! Available languages are {LANGS}.
Can't find your language? Please help us at @DoNotRepeat to translate the bot to your language. Create a new snippet Hey there!
I'm @DoNotRepeatBot. Never ever repeat the hassle of sending same message again! Please check /help for more information. If you are very new to me, you might wanna check /guide first 😁
<b>Syntax</b>
• <code>[ARG]</code> - <code>ARG</code> is optional and need not be provided.
• <code>&lt;ARG&gt;</code> - <code>ARG</code> is essential and must be provided.

<b>Commands</b>
• /add [<code>title</code>]
This command creates a new snippet with title provided.
If title is not provided, then the first few characters of the snippet body is used a title. If used as it is, I will prompt you for snippet. If the command is a reply to a message, then that message is used.
A message to be made snippet can be normal message or file (audio, photo, video etc.) or a sticker. Title is mandatory if the message doesn't have any textual content.

• /clear
Clear all the snippets of the chat.
Be careful before using it!

• /del <code>&lt;title&gt;</code>
Delete the snippet with given title.

• /done
Finish import of snippets.

• /get <code>&lt;title&gt;</code>
Get the snippet of given title.
Equivalent to <code>#title</code> or inline mode.

• /guide
Present a beginner friendly tutorial.

• /help
The very same help message.

• /import
Start the import process.
Using <i>import</i>, you can add multiple snippets without individual /add.
First send /import and send (or forward) messages to added. The title is automatically obtained from first few characters of the textual content. Use /done to finish the import.

• /lang <code>[lang]</code>
Change my language to <code>lang</code>.
Send the command without any language to view available languages.

• /list
List the snippets associated with the chat.
Tap the title to view the snippet.

• /start
Start the adventure.

<b>Inline Mode</b>
Type @DoNotRepeatBot in a chat and press space.
I will show you available snippets which you can filter by typing title or text of the snippet.

<b>Text</b>
Use #hashtag notation to get snippets via title.
For example, #hello will send snippet named <code>hello</code>

<b>Notes</b>
1. Addition, deletion and other manipulation tasks require the user to be an admin in groups.
2. Language is automatically set to the language the user uses. For groups it is always set to English unless changed by an admin.

You can learn more about the bot by using the <a href='https://github.come/j-arun-mani/DoNotRepeatBot'>documentation</a>.
There is also /help to give you overview of available commands and methods.
Finally, feel free to tell your thoughts and feedback in @DoNotRepeat 😉! Language has been set to <code>{LANG}</code>. Mass send me the messages to be added as snippets. Use /done to signal finish. Send me the snippet to add. Something went wrong. Yes, I won't tell you what happened though. That's not how you start me … Need some /help? The command should be a reply to a valid message. There are no snippets associated with this chat. Title is required! Either mention it directly or the message you replied to should have a textual content. You are not allowed to perform this action. • <a href='{LINK}?start={ID}{LOAD}'>{TITLE}</a> • Chat ID : <code>{CHAT_ID}</code>
• Snippets : <code>{COUNT}</code>
• Language : <code>{LANG}</code> 