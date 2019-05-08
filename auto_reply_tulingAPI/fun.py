# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()

# my_friend = bot.friends().search('书晗', sex=FEMALE, city="深圳")[0]

# 发送文本给好友
# my_friend.send('Hello WeChat!')
# 发送图片
# my_friend.send_image('my_picture.jpg')

bot.file_helper.send('Hello from wxpy!')