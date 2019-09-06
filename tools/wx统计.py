#coding=utf-8
import itchat
from itchat.content import TEXT
from itchat.content import *
import sys
import time
import re
reload(sys)
sys.setdefaultencoding('utf8')
import os

@itchat.msg_register([TEXT,PICTURE,FRIENDS,CARD,MAP,SHARING,RECORDING,ATTACHMENT,VIDEO],isGroupChat=True)
def receive_msg(msg):
    groups  = itchat.get_chatrooms(update=True)
    friends = itchat.get_friends(update=True)
    print "群数量:",len(groups)
    for i in range(0,len(groups)):
        print i+1,"--",groups[i]['NickName'],groups[i]['MemberCount'],"人"
    print "好友数量",len(friends)-1

    a = 0   # 不能统计
    b = 0   # 男
    c = 0   # 女

    for f in range(1,len(friends)):#第0个好友是自己,不统计
        if friends[f]['RemarkName']: # 优先使用好友的备注名称，没有则使用昵称
            user_name = friends[f]['RemarkName']
        else:
            user_name = friends[f]['NickName']
        sex = friends[f]['Sex']
        print f,"--",user_name,sex

        if sex == 0:
            a = a+1
        if sex == 1:
            b = b+1
        if sex == 2:
            c = c+1
    print a,b,c

itchat.auto_login(hotReload=True)
itchat.run()