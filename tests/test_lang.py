from DoNotRepeatBot.constants.message import Message
from DoNotRepeatBot.utils import gettext

g = gettext.GetText('zh-CN')
for k, v in Message.__dict__.items():
    if not k.startswith('_'):
        print(g.get(v))
        print('--------')
