��          �      �        �   	  1   �  &   �  D     <  F  ,   �  #   �  �   �     U	  �   j	  �	  �	  -   �  N   �       A   (  0   j  1   �  0   �  j   �  +   i  1   �  k   �  J  3  }   ~  '   �  $   $  C   I  v  �  !     !   &  n   H     �  {   �  �	  I  %   �(  @   �(  '   @)  3   h)  @   �)     �)     �)  Z   *     s*  1   �*  u   �*                                                                    
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
• Language : <code>{LANG}</code> Project-Id-Version: 3.0
Report-Msgid-Bugs-To: 
PO-Revision-Date: 2024-05-04 18:35+0530
Last-Translator: student_2333 <lgc2333@126.com>
Language-Team: Simplified Chinese
Language: Simplified Chinese
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Plural-Forms: nplurals=2; plural=(n > 1);
 <b>导入完成</b>
• 总计：<code>{TOTAL}</code>
• 成功：<code>{IMPORTED}</code>
• 失败：<code>{FAILED}</code> 成功添加便签 <code>{TITLE}</code> 已删除便签 <code>{TITLE}</code> 未找到 <code>{TITLE}</code>。使用 /list 查看所有便签。 @DoNotRepeatBot 可以让在你需要时在多个地方分享信息，而不用重新输入。
如果你有一条信息碰巧要在多个聊天中重复发送，你只需要将该信息保存到“<i>收藏夹</i>”中，并在每次需要时转发即可。
@DoNotRepeatBot 也可以做到，不过包含额外的功能，而且更加精简！

<b>开始使用</b>
让我们先从一个简单的例子开始。试着私聊Bot，发送指令<code>/add hello</code>。
然后Bot将会询问你要储存的消息。只需要简单地发送一条文本消息就好，至于是什么，那就看你的创造力了！

Bot应该会回复已经储存了你刚刚发送的消息

接着在聊天框里输入 @DoNotRepeatBot，按一下<code>空格键（Space）</code>，再输入<i>hello</i>。
Bot会显示你刚刚储存的便签，只需要点一下，Bot就会替你发送到当前的对话！使用起来就是这么简单！

如果你没有看到便签，请确保你输入的便签标题准确无误；或者等一会再尝试，因为Telegram可能会将之前查询的结果<i>缓存下来</i>。
我们仅仅讲了Bot能实现的一部分功能！

想了解Bot的更多信息，请查看<a href='https://github.come/j-arun-mani/DoNotRepeatBot'>文档</a>。
也可以使用 /help 查看可用的指令和功能。
最后，随时可以在 @DoNotRepeat 向我反馈Bug或者提出建议😉！ 无法将该消息作为便签。 成功清空所有已储存便签 可用语言：{LANGS}.
找不到你的语言？请在 @DoNotRepeat 帮助我们将Bot翻译为您的语言。 创建一个新便签 你好！
我是 @DoNotRepeatBot。再也不用麻烦地重复输入相同的消息了！使用 /help 查看更多信息。 如果你是新用户，不妨先试试 /guide 😁
<b>指令语法</b>
• <code>[参数]</code> - 该<code>参数</code>是可选的，可以不用提供。
• <code>&lt参数&gt</code> - 该<code>参数</code>是必选的，必须提供。

<b>指令列表</b>
• /add <code>[标题]</code>
此命令使用提供的标题储存一条新便签。
如果没有提供标题，那么将会使用消息的前几个字符作为标题。如果按原样输入，我就会提示该便签。如果使用该指令时回复了一条消息，那么该消息将会被作为便签内容
普通的文本消息、文件（音频，图片，视频等等）、贴纸都可以作为便签储存。如果消息没有文本内容则必须提供标题

• /clear
清除对话中所有已保存的便签。
用前请三思！

• /del <code>&lt标题&gt</code>
删除对话中指定标题的便签。

• /done
结束导入便签。

• /get <code>&lt标题&gt</code>
获取指定标题的便签。
与“<code>#标题</code>”和内联模式相同。

• /guide
提供一个对初学者友好的教程。

• /help
和这条一样的帮助消息。

• /import
进入导入消息模式。
使用<i>导入</i>，你可以添加多个便签而不需要单独发送 /add 指令。
首先发送 /import 然后发送（或者转发）消息来添加。将会自动使用消息的前几个字符作为标题。使用 /done 结束导入。

• /lang <code>[语言代码]</code>
将我的语言更改到<code>语言代码</code>。
发送不带参数的指令浏览可用语言列表

• /list
列出对话中所有已保存的便签。
点击标题浏览便签内容。

• /start
开始使用Bot。

<b>内联模式</b>
在对话中输入 @DoNotRepeatBot 后按空格键。
我将会显示所有可用的便签。你也可以使用标题或者内容筛选。

<b>文本消息</b>
使用 #标题 格式来获取指定标题的便签内容。
示例：#hello 将会发送名为<code>hello</code>的便签。

<b>提示</b>
1. 在群组中进行添加，删除等操作需要管理员权限。
2. Bot所用的语言会自动设置为用户所用的语言。群聊将会默认设置为英语，除非管理员切换。

想了解Bot的更多信息，请查看<a href='https://github.come/j-arun-mani/DoNotRepeatBot'>文档</a>。
也可以使用 /help 查看可用的指令和功能。
最后，随时可以在 @DoNotRepeat 向我反馈Bug或者提出建议😉！ 语言已设为<code>{LANG}</code>。 请批量发送要储存的消息，使用 /done 结束导入。 请发送需要添加的便签内容。 出错了！但我不会告诉你发生了什么。 并不是这样操作的……需要帮助吗？试试 /help 。 请回复一条有效信息。 该对话中没有便签。 必须提供标题！除非显式提供标题或者回复的内容中含有文本内容。 权限不足。 • <a href='{LINK}?start={ID}{LOAD}'>{TITLE}</a> • 对话 ID：<code>{CHAT_ID}</code>
• 便签数量：<code>{COUNT}</code>
• 当前语言：<code>{LANG}</code> 