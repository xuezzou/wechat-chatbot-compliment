# -*- coding:utf-8 -*- 

import itchat, re
from itchat.content import *
import random


@itchat.msg_register([TEXT], isGroupChat=True)
def text_reply(msg):
    # group_name的值修改成你要夸的weixin群名
    group_name = '夸夸';
    if msg['User']['NickName'] == group_name:
        print('Message from: %s' % msg['User']['NickName'])
        # 发送者的昵称
        username = msg['ActualNickName']
        print('Who sent it: %s' % username)
        print('-+-+'*5)

        test_bot = kuakuaChat()
        user_input = msg['Text'];
        answer_list = test_bot.answer_question(user_input)
        response = random.choice(answer_list)
        itchat.send('@' + '%s\n%s' % (username, response), msg['FromUserName'])

# Windows系统，enableCmdQR=True
# itchat.auto_login(enableCmdQR=True, hotReload=True)
# Mac、Linux，enableCmdQR=2

itchat.auto_login(enableCmdQR=2, hotReload=True)
itchat.run()
