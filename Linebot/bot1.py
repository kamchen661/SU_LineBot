# -*- coding: utf-8 -*-
from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, urllib, urllib.parse,timeit,atexit,youtube_dl,pafy
from threading import Thread
####################################################
botStart = time.time()
####################################################

####################################################
cl = LINE("")
####################################################

####################################################
cl.sendMessage("MID",'[自動發送]\n半垢登入成功\n作者:ÄñŁïäń\n作者網址:https://line.me/ti/p/~')
####################################################

####################################################
oepoll = OEPoll(cl)
####################################################

####################################################
readOpen = codecs.open("read.json","r","utf-8")
read = json.load(readOpen)
####################################################
settingsOpen = codecs.open("temp.json","r","utf-8")
settings = json.load(settingsOpen)
####################################################
redOpen = codecs.open("red.json","r","utf-8")
red = json.load(redOpen)
####################################################
jgOpen = codecs.open("jg.json","r","utf-8")
jg = json.load(jgOpen)
####################################################

####################################################
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
####################################################

####################################################
lineSettings = cl.getSettings()
clMID = cl.profile.mid
clProfile = cl.getProfile()
clSetting = cl.getSettings()
####################################################

####################################################
bl = ["MID"]
myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus
####################################################

####################################################
admin=[clMID]
King = "MID"
####################################################

####################################################
msg_dict = {}
msg_dictt = {}
####################################################

####################################################
wait = {
    'logout': {},
    'rapidFire': {},
    'group': "",
    'getmid': False,
    'um': False,#收回高速
    'cvp': False,#更換頭貼
    'gbc':{},
    'resset': False#偵測更新
    }
####################################################

####################################################
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}
####################################################

####################################################
setTime = {}
setTime = wait2['setTime']
####################################################

####################################################
profile = cl.getProfile()
####################################################

####################################################
msg_dict = {}
msg_dictt = {}
####################################################

####################################################
mulai = time.time()
####################################################

def Runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d 天\n%02d 時\n%02d 鐘\n%02d 秒\n以上為半垢機体運行時間\n半垢 運行時間測試' % (days, hours, mins, secs)
def Rtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d 天 %02d 時 %02d 鐘 %02d 秒' % (days, hours, mins, secs)
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def restartBot():
    print ("[ 訊息 ] 機器重啟")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = jg
        f = codecs.open('jg.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False    
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    cl.log("[ 錯誤 ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Yi  遭標註者出來'
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendMessageTag(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Yi  此人在群組(私聊)標住您'
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendMessagegat(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Yi  157.9出來'
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@MiliSun "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mid")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0) 
def ytdl(url):
    video = pafy.new(url)
    best = video.getbest() 
    best.download(filepath="test.mp4")
def gettoken(to):
    try:
        k1 = LINE() 
        cl.sendMessage(to,str(k1.authToken))
    except:
        pass
    return True
def help():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('help.txt', 'r') as f:
        text = f.read()
    help = text.format(key=key.title())
    return help
def help1():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('help1.txt', 'r') as f:
        text = f.read()
    help1 = text.format(key=key.title())
    return help1
def help2():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('help2.txt', 'r') as f:
        text = f.read()
    help2 = text.format(key=key.title())
    return help2
def help3():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('help3.txt', 'r') as f:
        text = f.read()
    help3 = text.format(key=key.title())
    return help3
def help4():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('help4.txt', 'r') as f:
        text = f.read()
    help4 = text.format(key=key.title())
    return help4
def help5():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('help5.txt', 'r') as f:
        text = f.read()
    help5 = text.format(key=key.title())
    return help5
def unsend(msgid):
    sleep(1)
    cl.unsendMessage(msgid)
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 1:
            print ("更新配置文件")
        if op.type == 2:
            contact = cl.getContact(op.param1)
            if wait["resset"] == True:
                if op.param2 == "2":
                    cl.sendMessage(op.param1,"[自動發送]\n抓到更改名稱摟!!!\n作者:孫孫\n作者網址:https://line.me/ti/p/~yiling_0721_bot\n禁止抄襲@!\n禁止抄襲@!\n禁止抄襲@!\n申明三次")
                    cl.sendMessage("MID","通知好友更改名稱:\n" + contact.displayName)
                if op.param2 == "8":
                    cl.sendMessage(op.param1,"[自動發送]\n抓到更改頭貼/動態頭貼摟!!!\n作者:孫孫\n作者網址:https://line.me/ti/p/~yiling_0721_bot\n禁止抄襲@!\n禁止抄襲@!\n禁止抄襲@!\n申明三次")
                    cl.sendMessage("MID","通知好友更改動態頭貼:\n" + contact.displayName)
                if op.param2 == "16":
                    cl.sendMessage(op.param1,"[自動發送]\n抓到更改個簽摟!!!\n作者:孫孫\n作者網址:https://line.me/ti/p/~yiling_0721_bot\n禁止抄襲@!\n禁止抄襲@!\n禁止抄襲@!\n申明三次")
                    cl.sendMessage("MID","通知好友更改個簽:\n" + contact.displayName)
        if op.type == 5:
            contact = cl.getContact(op.param1)
            print ("[ 5 ] 通知添加好友 名字: " + contact.displayName)
            if settings["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
        if op.type == 11:
            group = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            if settings["qrprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    cl.sendMessage(op.param1,cl.getContact(op.param2).displayName + "網址保護中...不要動群組網址！")
                    cl.sendMessage("MID",cl.getContact(op.param2).displayName + "網址保護中...不要動群組網址！")
        if op.type == 13:
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            group = cl.getGroup(op.param1)
            if clMID in op.param3:
                if settings["autoJoin"] == True:
                    try:
                        arrData = ""
                        text = "%s "%('[進群通知]\n')
                        arr = []
                        mention = "@Mili "
                        slen = str(len(text))
                        elen = str(len(text) + len(mention) - 1)
                        arrData = {'S':slen, 'E':elen, 'M':op.param2}
                        arr.append(arrData)
                        text += mention + "\n半垢公開招待使用中.....\n感謝您的邀請!!!\n公開半垢作者:ÄñŁïäń\n作者網址:https://line.me/ti/p/~bestissac1234567890"
                        cl.acceptGroupInvitation(op.param1)
                        cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        cl.sendContact(op.param1, "MID")
                        cl.sendMessage('MID',"通知邀請群組:\n" + str(group.name)+"群組 \n"+ str(group.id)+ "\n邀請者:\n" + contact1.displayName + "\nMID\n" + contact1.mid)
                    except Exception as error:
                        print(error)
        if op.type == 15:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            if settings["seeLeave"] == True:
                try:
                    arrData = ""
                    text = "%s "%('[提示]\n')
                    arr = []
                    mention = "@Mili "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + "退出了 {} 群組 離我們而去了OAO！".format(str(group.name))
                    cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
        if op.type == 17:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            if settings["seeJoin"] == True:
                try:
                    arrData = ""
                    text = "%s "%('歡迎')
                    arr = []
                    mention = "@Mili "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + "您加入 {} 我們的小窩！".format(str(group.name))
                    cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
            if op.param1 in jg["JoinGroup"]:
                if op.param2 not in admin:
                    try:
                        contact = cl.getContact(op.param2)
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except Exception as e:
                        print(e)
        if op.type == 19:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            contact2 = cl.getContact(op.param3)
            print ("[19]有人把人踢出群組 群組名稱: " + str(group.name) + "\n" + op.param1 +"\n踢人者: " + contact1.displayName + "\nMid:" + contact1.mid + "\n被踢者: " + contact2.displayName + "\nMid:" + contact2.mid )
            cl.sendMessage("MID","有人把人踢出群組 群組名稱: " + str(group.name) + "\n" + op.param1 +"\n踢人者: " + contact1.displayName + "\nMid:" + contact1.mid + "\n被踢者: " + contact2.displayName + "\nMid:" + contact2.mid )
            if settings["protect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    if settings["kickContact"] == True:
                        try:
                            arrData = ""
                            text = "%s " %('[警告]')
                            arr = []
                            mention1 = "@Mili "
                            slen = str(len(text))
                            elen = str(len(text) + len(mention1) - 1)
                            arrData = {'S':slen, 'E':elen, 'M':op.param2}
                            arr.append(arrData)
                            text += mention1 + '踢了 '
                            mention2 = "@Mili "
                            sslen = str(len(text))
                            eelen = str(len(text) + len(mention2) - 1)
                            arrdata = {'S':sslen, 'E':eelen, 'M':op.param3}
                            arr.append(arrdata)
                            text += mention2
                            cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        except Exception as error:
                            print(error)
            else:
                if settings["kickContact"] == True:
                    try:
                        arrData = ""
                        text = "%s " %('[警告]')
                        arr = []
                        mention1 = "@Mili "
                        slen = str(len(text))
                        elen = str(len(text) + len(mention1) - 1)
                        arrData = {'S':slen, 'E':elen, 'M':op.param2}
                        arr.append(arrData)
                        text += mention1 + '踢了 '
                        mention2 = "@Mili "
                        sslen = str(len(text))
                        eelen = str(len(text) + len(mention2) - 1)
                        arrdata = {'S':sslen, 'E':eelen, 'M':op.param3}
                        arr.append(arrdata)
                        text += mention2
                        cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                    except Exception as error:
                        print(error)
        if op.type == 24:
            print ("[ 24 ] 通知離開副本")
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 1:
            print ("[1]更新配置文件")
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver 
            if sender in admin:
                pass 
            else:
                if msg.to in wait["rapidFire"]:
                    if time.time() - wait["rapidFire"][msg.to] < 2:
                        return
                    else:
                        wait["rapidFire"][msg.to] = time.time()
                else:
                    wait["rapidFire"][msg.to] = time.time()       
            if msg.contentType == 0:
                if text is None:
                    return
                else:
                    cmd = text.lower()
            if msg.contentType == 1:
                if sender in wait['gbc'] and wait['gbc'][sender]['type'] == 'pic':
                    image = cl.downloadObjectMsg(msg.id )
                    n = cl.getGroupIdsJoined()
                    g = 0
                    for manusia in n:
                        group = cl.getGroup(manusia)
                        nama =[contact.mid for contact in group.members]
                        if len(nama) >int(wait['gbc'][sender]['over'] ):
                            cl.sendMessage(manusia,"➲➲➲群組廣播➲➲➲➲ 《圖片》\n" + wait['gbc'][sender]['text'] )
                            cl.sendImage(manusia,image)
                            g+=1
                        else:
                            pass
                    cl.sendMessage(to,"➲➲➲群組廣播➲➲➲➲ 分享《{}》個群組".format(str(g)))
                    cl.deleteFile(image)
                    del wait['gbc'][sender]
            if msg.contentType == 13:
                if sender in wait['gbc'] and wait['gbc'][sender]['type'] == 'contact':
                    mid =msg.contentMetadata["mid"]
                    n = cl.getGroupIdsJoined()
                    g = 0
                    for manusia in n:
                        group = cl.getGroup(manusia)
                        nama =[contact.mid for contact in group.members]
                        if len(nama) >int(wait['gbc'][sender]['over'] ):
                            cl.sendMessage(manusia,"➲➲➲群組廣播➲➲➲➲ 《友資》\n" + wait['gbc'][sender]['text'] )
                            cl.sendContact(manusia,mid)
                            g+=1
                        else:
                            pass
                    cl.sendMessage(to,"➲➲➲群組廣播➲➲➲➲ 分享《{}》個群組".format(str(g)))
                    del wait['gbc'][sender]
            if msg.contentType == 16:
                if sender in wait['gbc'] and wait['gbc'][sender]['type'] == 'post':
                    postid =str(msg.contentMetadata['postEndUrl']).split("&postId=")[1]
                    n = cl.getGroupIdsJoined()
                    g = 0
                    for manusia in n:
                        group = cl.getGroup(manusia)
                        nama =[contact.mid for contact in group.members]
                        if len(nama) >int(wait['gbc'][sender]['over'] ):
                            cl.sendMessage(manusia,"➲➲➲群組廣播➲➲➲➲ 《貼文》\n" + wait['gbc'][sender]['text'] )
                            cl.sendPostToTalk(manusia,postid)
                            g+=1
                        else:
                            pass
                    cl.sendMessage(to,"➲➲➲群組廣播➲➲➲➲ 分享《{}》個群組".format(str(g)))
                    del wait['gbc'][sender]
            if sender in admin:
				#指令表txt版本
                if text.lower() == 'help':
                        cl.relatedMessage(to, help(),op.message.id)
                elif text.lower() == 'help1':
                        cl.relatedMessage(to, help1(),op.message.id)
                elif text.lower() == 'help2':
                        cl.relatedMessage(to, help2(),op.message.id)
                elif text.lower() == 'help3':
                        cl.relatedMessage(to, help3(),op.message.id)
                elif text.lower() == 'help4':
                        cl.relatedMessage(to, help4(),op.message.id)
                elif text.lower() == 'help5':
                        cl.relatedMessage(to, help5(),op.message.id)
                elif text.lower() in ['rg']:				
                    G = cl.getGroup(msg.to)
                    group = cl.getGroup(to)
                    contact = cl.getContact(sender)
                    gtime = group.createdTime
                    gtimee = int(round(gtime/1000))
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "創群者已砍帳"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                         gPending = str(len(group.invitee))				
                    ret_ ="☲☲☲☲☲群組☲☲☲☲☲"
                    ret_ +="\n成員數量\n【"+(str(len(group.members)))+"】"
                    ret_ +="\n邀請數量\n【"+(gPending)+"】"
                    ret_ +="\n☲☲☲☲☲群組☲☲☲☲☲"
                    ret_ +="\n群組名稱\n【{}】".format(str(group.name))
                    ret_ +="\n☲☲☲☲☲☲☲☲☲☲☲☲"
                    ret_ +="\n群組建立時間\n【{}】".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(gtimee)))
                    ret_ +="\n☲☲☲☲☲說明☲☲☲☲☲"
                    ret_ +="\n群主創建者"
                    ret_ +="\n【"+(str(gCreator))+"】"
                    ret_ +="\n☲☲☲☲☲☲☲☲☲☲☲☲"
                    ret_ +="\n群組Gid"
                    ret_ +="\n【{}】".format(group.id)
                    ret_ +="\n☲☲☲☲☲☲☲☲☲☲☲☲"
                    cl.relatedMessage(to, str(ret_),op.message.id)
                elif text.lower() == 'rlb':
                    a = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    b = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    c = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    d = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    e = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    f = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    g = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    h = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    i = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    j = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    k = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    l = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    m = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    n = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    o = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    slot = "拉霸機拉霸一次\n第一行==>{}  {}  {}<==\n第二行==>{}  {}  {}<==\n第三行==>{}  {}  {}<==\n第四行==>{}  {}  {}<==\n第五行==>{}  {}  {}<==\n以上是您的拉霸結果".format(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o)
                    cl.relatedMessage(to,slot,op.message.id)
                    if a == e == i == j == o:
                        cl.relatedMessage(to,"[自動回覆]\n恭喜拉霸機中獎~~",op.message.id)
                        return
                    cl.relatedMessage(to,"[自動回覆]\n可惜啦ww再試一次吧w",op.message.id)	
                elif msg.text in ["本日運勢","rls"]:
                    a = random.choice(["大吉！！！運氣旺！ヽ(✿ﾟ▽ﾟ)ノ","中吉！運氣好～(ﾟ∀ﾟ)","小吉〜小有手氣(`・ω・´)","末吉〜還可以(,,・ω・,,)","吉〜普普通通～(´･ω･`)","凶〜有點不好(つд⊂)","大凶〜有點悲劇｡･ﾟ･(ﾉД`)ヽ(ﾟДﾟ )"])
                    slot = "您今天的運氣\n{}<==\n以上是您的測試運氣結果".format(a)
                    cl.relatedMessage(to,slot,op.message.id)
                    cl.relatedMessage(to,"[自動回覆]\n在測試一次吧！ヽ(✿ﾟ▽ﾟ)ノ",op.message.id)	
                #防翻保護
                elif "/ti/g/" in msg.text.lower():
                    if settings["autoJoinTicket"] == True:
                        link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                        links = link_re.findall(text)
                        n_links = []
                        for l in links:
                            if l not in n_links:
                                n_links.append(l)
                        for ticket_id in n_links:
                            group = cl.findGroupByTicket(ticket_id)
                            cl.acceptGroupInvitationByTicket(group.id,ticket_id)
			    #少數重要功能
                elif text.lower() == 'rs':
                    cl.relatedMessage(to, "重新啟動中....",op.message.id)	
                    restartBot()
                elif text.lower() == 'rt':
                    eltime = time.time() - mulai
                    bot = "運行時間長達\n" +Runtime(eltime)
                    cl.relatedMessage(msg.to,bot,op.message.id)	
                elif text.lower() == 'save':
                    backupData()
                    cl.relatedMessage(to,"儲存設定成功!",op.message.id)
                elif text.lower() == 'bye':
                    if msg.toType == 2:
                        ginfo = cl.getGroup(to)
                        try:
                            cl.leaveGroup(to)
                        except:
                            pass
				#進群退群退副本
                elif text.lower() == 'aj on':
                    settings["autoJoin"] = True
                    cl.relatedMessage(to, "自動加入群組已開啟 ✔",op.message.id)	
                elif text.lower() == 'aj off':
                    settings["autoJoin"] = False
                    cl.relatedMessage(to, "自動加入群組已關閉 ✘",op.message.id)	
                elif text.lower() == 'al on':
                    settings["autoLeave"] = True
                    cl.relatedMessage(to, "自動離開副本已開啟 ✔",op.message.id)	
                elif text.lower() == 'al off':
                    settings["autoLeave"] = False
                    cl.relatedMessage(to, "自動離開副本已關閉 ✘",op.message.id)	
                elif text.lower() == 'qj on':
                    settings["autoJoinTicket"] = True
                    cl.relatedMessage(to, "網址自動入群已開啟 ✔",op.message.id)	
                elif text.lower() == 'qj off':
                    settings["autoJoinTicket"] = False
                    cl.relatedMessage(to, "網址自動入群已關閉 ✘",op.message.id)	
				#其餘加好友收回自動已讀
                elif text.lower() == 'ad on':
                    settings["autoAdd"] = True
                    cl.relatedMessage(to, "自動加入好友已開啟 ✔",op.message.id)	
                elif text.lower() == 'ad off':
                    settings["autoAdd"] = False
                    cl.relatedMessage(to, "自動加入好友已關閉 ✘",op.message.id)	
                elif text.lower() == 'rr on':
                    settings["reread"] = True
                    cl.relatedMessage(to, "查詢收回開啟 ✔",op.message.id)	
                elif text.lower() == 'rr off':
                    settings["reread"] = False
                    cl.relatedMessage(to, "查詢收回關閉 ✘",op.message.id)	
                elif text.lower() == 'rd on':
                    settings["autoRead"] = True
                    cl.relatedMessage(to, "自動已讀已開啟 ✔",op.message.id)	
                elif text.lower() == 'rd off':
                    settings["autoRead"] = False
                    cl.relatedMessage(to, "自動已讀已關閉 ✘",op.message.id)	
				#更改顯示
                elif text.lower() == 'c on':
                    wait["resset"] = True
                    cl.relatedMessage(to, "偵測更新帳號\n名子✘/圖片✘/個簽✘\n更新為開啟偵測狀態✔\n名子✔/圖片✔/個簽✔",op.message.id)	
                elif text.lower() == 'c off':
                    wait["resset"] = False
                    cl.relatedMessage(to, "偵測更新帳號\n名子✔/圖片✔/個簽✔\n更新為關閉偵測狀態✘\n名子✘/圖片✘/個簽✘",op.message.id)	
				#踢人顯示
                elif text.lower() == 'kc on':
                    settings["kickContact"] = True
                    cl.relatedMessage(to, "踢人標註已開啟 ✔═",op.message.id)	
                elif text.lower() == 'kc off':
                    settings["kickContact"] = False
                    cl.relatedMessage(to, "踢人標註已關閉 ✘═",op.message.id)	
				#進群退群
                elif text.lower() == 'sj on':
                    settings["seeJoin"] = True
                    cl.relatedMessage(to, "入群通知已開啟 ✔═",op.message.id)	
                elif text.lower() == 'sj off':
                    settings["seeJoin"] = False
                    cl.relatedMessage(to, "入群通知已關閉 ✘═",op.message.id)	
                elif text.lower() == 'sl on':
                    settings["seeLeave"] = True
                    cl.relatedMessage(to, "退群通知已開啟 ✔═",op.message.id)	
                elif text.lower() == 'sl off':
                    settings["seeLeave"] = False
                    cl.relatedMessage(to, "退群通知已關閉 ✘═",op.message.id)	
                elif text.lower() == 'm on':
                    settings["detectMention"] = False
                    cl.relatedMessage(to, "標註回覆已開啟 ✔",op.message.id)	
                elif text.lower() == 'm off':
                    settings["detectMention"] = True
                    cl.relatedMessage(to, "標註回覆已關閉 ✘",op.message.id)	
                elif text.lower() == 'ru on':
                    wait["um"] = True
                    cl.relatedMessage(to, "收回已開啟 ✔",op.message.id)	
                elif text.lower() == 'ru off':
                    wait["um"] = False
                    cl.relatedMessage(to, "收回已關閉 ✘",op.message.id)	
				#保護項目
                elif text.lower() == 'pro on':
                    settings["protect"] = True
                    cl.relatedMessage(to, "群組保護已開啟 ✔",op.message.id)
                elif text.lower() == 'pro off':
                    settings["protect"] = False
                    cl.relatedMessage(to, "群組保護已關閉 ✘",op.message.id)
                elif text.lower() == 'ip on':
                    settings["inviteprotect"] = True
                    cl.relatedMessage(to, "群組邀請保護已開啟 ✔",op.message.id)
                elif text.lower() == 'ip off':
                    settings["inviteprotect"] = False
                    cl.relatedMessage(to, "群組邀請保護已關閉 ✘",op.message.id)
                elif text.lower() == 'qp on':
                    settings["qrprotect"] = True
                    cl.relatedMessage(to, "群組網址保護已開啟 ✔",op.message.id)
                elif text.lower() == 'qp off':
                    settings["qrprotect"] = False
                    cl.relatedMessage(to, "群組網址保護已關閉 ✘",op.message.id)
                elif text.lower() in ['rk on']:
                    if msg.toType ==2:
                        jg["JoinGroup"][to] = True
                        cl.relatedMessage(to, "進群保護開啟 ✔",op.message.id)
                elif text.lower() in ['rk off']:
                    if msg.toType ==2 :
                        try:
                            del jg["JoinGroup"][to]
                            cl.relatedMessage(to, "進群保護關閉 ✘",op.message.id)
                        except:
                            cl.relatedMessage(to, "沒有開啟進群保護關閉 ✘",op.message.id)
				#機器開關查詢
                elif text.lower() == 'set':
                    try:
                        ret_ = "ÄñŁïäń Set List"
                        ret_ += "\n進群類型 開關"
                        if settings["autoJoin"] == True: ret_ += "\n自動入群 ✅"
                        else: ret_ += "\n自動入群 ❌"
                        if settings["autoJoinTicket"] == True: ret_ += "\n網址入群 ✅"
                        else: ret_ += "\n網址入群 ❌"
                        if settings["autoLeave"] == True: ret_ += "\n自離副本 ✅"
                        else: ret_ += "\n自離副本 ❌"
                        ret_ += "\n其餘功能 開關"
                        if settings["autoAdd"] == True: ret_ += "\n自動加友 ✅"
                        else: ret_ += "\n自動加友 ❌"
                        if settings["autoRead"] == True: ret_ += "\n自動已讀 ✅"
                        else: ret_ += "\n自動已讀 ❌"
                        if settings["reread"] == True: ret_ += "\n查詢收回 ✅"
                        else: ret_ += "\n查詢收回 ❌"
                        if wait["resset"] == True: ret_ += "\n偵測更改 ✅"
                        else: ret_ += "\n偵測更改 ❌"
                        ret_ += "\n保護類型 開關"
                        if settings["protect"] == True: ret_ += "\n群組保護 ✅"
                        else: ret_ += "\n群組保護 ❌"
                        if settings["inviteprotect"] == True: ret_ += "\n邀請保護 ✅"
                        else: ret_ += "\n邀請保護 ❌"
                        if settings["qrprotect"] == True: ret_ += "\n網址保護 ✅"
                        else: ret_ += "\n網址保護 ❌"
                        ret_ += "\n通知類型 開關"
                        if settings["seeJoin"] == True: ret_ += "\n入群通知開啟 ✅"
                        else: ret_ += "\n入群通知關閉 ❌"
                        if settings["seeLeave"] == True: ret_ += "\n退群通知開啟 ✅"
                        else: ret_ += "\n退群通知關閉 ❌"
                        if msg.toType==2:
                            ret_ += "\nÄñŁïäń Group Set List"
                            G = cl.getGroup(msg.to)
                            ret_ += "\n群組名稱\n<{}>".format(str(G.name))
                            ret_ += "\n進群保護 開關"
                            if G.id in jg["JoinGroup"] : ret_+="\n進群保護 ✅"
                            else: ret_ += "\n進群保護 ❌"
                        ret_ += "\n作者:超音速
                        ret_ += "\nID: bestissac1234567890"
                        ret_ += "\nQR:http://line.me/ti/p/~bestissac1234567890"
                        ret_ += "\n<查詢完畢>"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
				#機器簡介
                elif text.lower() == 'about':
                    try:
                        cl.kickoutFromGroup(to,["HEY"])
                        cl.inviteIntoGroup(to, ["HEY"])
                    except Exception as e:
                        if e.reason == "request blocked":
                            aa = "無法執行(規制)"
                        else:
                            aa = "可以執行(無規制)"
                        arr = []
                        t1 = time.time()
                        cl.sendMessage("MID", "About檢查中......")
                        t2 = (time.time() - t1)/100
                        owner = "MID"
                        creator = cl.getContact(owner)
                        contact = cl.getContact(clMID)
                        grouplist = cl.getGroupIdsJoined()
                        contactlist = cl.getAllContactIds()
                        blockedlist = cl.getBlockedContactIds()
                        eltime = time.time() - mulai
                        bot = Rtime(eltime)
                        ret_ = "《關於自己》"
                        ret_ += "\n➲群組數量: {}".format(str(len(grouplist)))
                        ret_ += "\n➲好友人數: {}".format(str(len(contactlist)))
                        ret_ += "\n➲封鎖人數: {}".format(str(len(blockedlist)))
                        ret_ += "\n➲個簽字數: {}".format(str(len(clProfile.statusMessage)))
                        ret_ += "\n➲最愛人數: {}".format(str(len(cl.getFavoriteMids())))
                        ret_ += "\n➲封鎖好友: {}".format(str(len(cl.getBlockedContactIds())))
                        ret_ += "\n➲邀請群組: {}".format(str(len(cl.getGroupIdsInvited())))
                        ret_ += "\n➲Line帳號ID:\n➲{}".format(clProfile.userid)
                        ret_ += "\n➲個人名稱:\n➲{}".format(contact.displayName)
                        ret_ += "\n➲個人網址(一):\n➲http://line.me/ti/p/{}".format(str(clProfile.userid))
                        ret_ += "\n➲個人網址(二):\n➲http://line.me/ti/p/{}".format(str(clSetting.contactMyTicket))
                        ret_ += "\n➲識別碼:\n➲{}".format(str(clProfile.mid))
                        ret_ += "\n《狀態規制》"
                        ret_ += "\n➲踢人狀態: {}".format(aa)
                        ret_ += "\n➲邀請狀態: {}".format(aa)
                        ret_ += "\n➲取消狀態: 可以執行(無規制)"
                        ret_ += "\n《個人開關》"
                        if settings["autoJoin"] == True: ret_ += "\n➲自動入群 ✅"
                        else: ret_ += "\n➲自動入群 ❌"
                        if settings["autoJoinTicket"] == True: ret_ += "\n➲網址入群 ✅"
                        else: ret_ += "\n➲網址入群 ❌"
                        if settings["reread"] == True: ret_ += "\n➲防止收回 ✅"
                        else: ret_ += "\n➲防止收回 ❌"
                        if settings["autoRead"] == True: ret_ += "\n➲自動已讀 ✅"
                        else: ret_ += "\n➲自動已讀 ❌"
                        ret_ += "\n《關於半垢》"
                        ret_ += "\n➲商業半垢 V5.2"
                        ret_ += "\n➲半垢作者:超音速
                        ret_ += "\n➲半垢極限速度:\n➲{}".format(str(t2))
                        ret_ += "\n➲半垢運行時間:\n➲l───────●──────l\n➲{}\n➲⇆ ㅤ ㅤ◁  ㅤ❚ ❚  ㅤ▷  ㅤ↻".format(bot)
                        cl.relatedMessage(to, str(ret_),op.message.id)
                    except Exception as e:
                        cl.relatedMessage(msg.to, str(e),op.message.id)
                elif text.lower() == 'ru':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.relatedMessage(to, "[ 群組網址 ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)),op.message.id)
                        else:
                            cl.relatedMessage(to, "群組沒有開啟網址",op.message.id)
                elif text.lower() == 'code on':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            cl.relatedMessage(to, "群組網址已開",op.message.id)
                        else:
                            group.preventedJoinByTicket = False
                            cl.updateGroup(group)
                            cl.relatedMessage(to, "開啟成功",op.message.id)
                elif text.lower() == 'code off':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            cl.relatedMessage(to, "群組網址已關",op.message.id)
                        else:
                            group.preventedJoinByTicket = True
                            cl.updateGroup(group)
                            cl.relatedMessage(to, "關閉成功",op.message.id)
                elif text.lower().startswith("rt:"):
                    id = text[3:].split(':')
                    for x in range(int(id[1])):
                        cl.sendPostToTalk(to,id[0])
                    cl.relatedMessage(to, "文章分享完畢",op.message.id)
                elif text.lower().startswith("rpc:"):
                    separate = text.split(":")
                    bctxt = text.replace(separate[0] + ":","")
                    t = cl.getAllContactIds()
                    for manusia in t:
                        cl.sendMessage(manusia,bctxt[1])
                elif text.lower().startswith("rgb:"):
                    data = text[4:].lower().split(':')
                    if len(data) == 2:data.append("0")
                    elif len(data) >3 or len(data) <2:return
                    try:int(data[2])
                    except:return
                    if data[0] == 'text':
                        n = cl.getGroupIdsJoined()
                        g = 0
                        for manusia in n:
                            group = cl.getGroup(manusia)
                            nama =[contact.mid for contact in group.members]
                            if len(nama) >int(data[2]):
                                cl.sendMessage(manusia,"➲➲➲群組廣播➲➲➲➲ 《文字》\n" + data[1])
                                g+=1
                            else:
                                pass
                        cl.sendMessage(to,"➲➲➲群組廣播➲➲➲➲ 分享《{}》個群組".format(str(g)))
                    elif data[0] in ['pic', 'contact', 'post']:
                        wait['gbc'][sender] = {'type':data[0],'text':data[1],'over':data[2]}
                        cl.relatedMessage(to,'請發送你要廣播的東西~',op.message.id)
				#測速功能
                elif text.lower() == 'sp':
                    start = time.time()
                    cl.sendMessage("MID", "Test Speed......")
                    elapsed_time = time.time() - start
                    cl.relatedMessage(to,format(str(elapsed_time)) + " seconds",op.message.id)
                elif text.lower() == 'speed':
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    str1 = str(time0)
                    start = time.time()
                    cl.relatedMessage(to,'處理速度\n' + str1 + ' seconds',op.message.id)
                    elapsed_time = time.time() - start
                    cl.relatedMessage(to,'指令反應\n' + format(str(elapsed_time)) + '秒',op.message.id)
                elif text.lower() == 'spt':
                    start = time.time()
                    cl.sendMessage("MID", "Test Speed......")
                    elapsed_time = (time.time() - start)/100
                    cl.relatedMessage(to,format(str(elapsed_time)) + " seconds",op.message.id)
                elif text.lower() == 'spk':
                    start = time.time()
                    cl.sendMessage("MID", "Test Speed......")
                    elapsed_time = (time.time() - start)/100
                    cl.relatedMessage(to,"Kick One\n" + format(str(elapsed_time)) + "秒",op.message.id)
                elif msg.text in ["/sp","/speed"]:
                    t1 = time.time()
                    cl.sendMessage("MID", "First Term")
                    t2 = time.time() - t1
                    time.sleep(0.01)
                    t3 = time.time()
                    cl.sendMessage("MID", "Second Term")
                    t4 = time.time() - t3
                    time.sleep(0.01)
                    t5 = time.time()
                    cl.sendMessage("MID", "Third Term")
                    t6 = time.time() - t5
                    time.sleep(0.01)
                    t7 = time.time()
                    cl.sendMessage("MID", "Four Term")
                    t8 = time.time() - t7
                    time.sleep(0.01)
                    t9 = time.time()
                    cl.sendMessage("MID", "Firth Term")
                    t10 = time.time() - t9
                    time.sleep(0.01)
                    a1 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    b1 = str(a1)
                    a2 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    b2 = str(a2)
                    a3 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    b3 = str(a3)
                    a4 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    b4 = str(a4)
                    a5 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    b5 = str(a5)
                    ret_ = "     [反應速度]\n"
                    ret_ += "First:{}秒\n".format(str(t2))
                    ret_ += "Second:{}秒\n".format(str(t4))
                    ret_ += "Third:{}秒\n".format(str(t6))
                    ret_ += "Four:{}秒\n".format(str(t8))
                    ret_ += "Five:{}秒\n     [處理速度]\n".format(str(t10))
                    ret_ += "First:{}秒\n".format(str(b1))
                    ret_ += "Second:{}秒\n".format(str(b2))
                    ret_ += "Third:{}秒\n".format(str(b3))
                    ret_ += "Four:{}秒\n".format(str(b4))
                    ret_ += "Five:{}秒\n".format(str(b5))
                    ret_ += "     [Test ]"
                    cl.relatedMessage(to, str(ret_),op.message.id)
                    cl.relatedMessage("MID", str(ret_),op.message.id)
				#踢人指令
                elif text.lower().startswith("ri:"):
                    separate = text.split(":")
                    midd = text.replace(separate[0] + ":","")
                    cl.kickoutFromGroup(to,[midd])
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(to,[midd])
                elif text.lower().startswith("ti:"):
                    separate = text.split(":")
                    midd = text.replace(separate[0] + ":","")
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(to,[midd])
                elif text.lower().startswith("vk:"):
                    separate = text.split(":")
                    midd = text.replace(separate[0] + ":","")
                    cl.kickoutFromGroup(msg.to,[midd])
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
                    cl.cancelGroupInvitation(msg.to,[midd])
                elif msg.text.lower().startswith("kt "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                            cl.relatedMessage(to,"目前處於 帳號規制狀態中",op.message.id)
                elif msg.text.lower().startswith("ri "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.findAndAddContactsByMid(target)
                            cl.kickoutFromGroup(msg.to,[target])
                            cl.inviteIntoGroup(to,[target])
                        except:
                            cl.relatedMessage(to,"目前處於 帳號規制狀態中",op.message.id)
                elif msg.text.lower().startswith("ti "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.findAndAddContactsByMid(target)
                            cl.inviteIntoGroup(to,[target])
                        except:
                            cl.relatedMessage(to,"目前處於 帳號規制狀態中",op.message.id)
                elif msg.text.lower().startswith("vk "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                            cl.findAndAddContactsByMid(target)
                            cl.inviteIntoGroup(to,[target])
                            cl.cancelGroupInvitation(msg.to,[target])
                        except:
                            cl.relatedMessage(to,"目前處於 帳號規制狀態中",op.message.id)
                elif text.lower().startswith("tnk:"):
                        separate = text.split(":")
                        _name = text.replace(separate[0] + ":","")
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.relatedMessage(msg.to,"群組內沒有這個名稱",op.message.id)
                        else:
                            for target in targets:
                                try:
                                    cl.kickoutFromGroup(msg.to,[target])
                                except:
                                    pass
                elif text.lower() == 'mine':
                     try:
                         cl.kickoutFromGroup(msg.to, ["ÄñŁïäń_KICKING"])
                         cl.sendMessage(msg.to, "正常")
                     except Exception as e:
                         if e.reason == "request blocked":
                            me = cl.getContact(sender)
                            cl.relatedMessage(msg.to,"[查詢資料]\n"+"使用者名稱: "+me.displayName+"\n使用者Mid: "+sender+"\n踢人狀態: request blocked\n邀請狀態: request blocked\n取消狀態: 可以執行\n[完]",op.message.id)
                         else:
                            me = cl.getContact(sender)
                            cl.relatedMessage(msg.to,"[查詢資料]\n"+"使用者名稱: "+me.displayName+"\n使用者Mid: "+sender+"\n踢人狀態: 可以執行\n邀請狀態: 可以執行\n取消狀態: 可以執行\n[完]",op.message.id)
                elif msg.text == "me": cl.sendMessage(msg.to, text="播放歌曲資料\n作者名稱:"+cl.getContact(msg._from).displayName, contentMetadata={'previewUrl': 'http://dl.profile.line-cdn.net/' + cl.getContact(msg._from).pictureStatus, 'i-installUrl': 'line://nv/profilePopup/mid=' + msg._from, 'ORGCONTP': 'MUSIC', 'type': 'mt', 'subText': "\n歌手個簽:\n"+cl.getContact(msg._from).statusMessage, 'a-installUrl': 'http://google.com', 'a-packageName': 'jp.naver.line.music', 'playUrl': str(BeautifulSoup(requests.get("https://anonfile.com/y2l8Rb2bn9").text, "html.parser").find("a", id="download-url")['href']), 'countryCode': 'TW', 'a-linkUri': 'line://nv/profilePopup/mid=' + msg._from, 'i-linkUri': 'line://nv/profilePopup/mid=' + msg._from, 'text': cl.getContact(msg._from).displayName, 'id': 'mt000000000a6b79f9','linkUri': 'line://nv/profilePopup/mid=' + msg._from}, contentType=19)
                elif msg.text == "me1": cl.sendMessage(msg.to, text="播放歌曲資料\n作者名稱:"+cl.getContact(msg._from).displayName, contentMetadata={'previewUrl': 'http://dl.profile.line-cdn.net/' + cl.getContact(msg._from).pictureStatus, 'i-installUrl': 'line://nv/profilePopup/mid=' + msg._from, 'ORGCONTP': 'MUSIC', 'type': 'mt', 'subText': "\n歌手個簽:\n"+cl.getContact(msg._from).statusMessage, 'a-installUrl': 'http://google.com', 'a-packageName': 'jp.naver.line.music', 'playUrl': str(BeautifulSoup(requests.get("https://anonfile.com/a2n8Rf25nb").text, "html.parser").find("a", id="download-url")['href']), 'countryCode': 'TW', 'a-linkUri': 'line://nv/profilePopup/mid=' + msg._from, 'i-linkUri': 'line://nv/profilePopup/mid=' + msg._from, 'text': cl.getContact(msg._from).displayName, 'id': 'mt000000000a6b79f9','linkUri': 'line://nv/profilePopup/mid=' + msg._from}, contentType=19)
                elif msg.text == "me2": cl.sendMessage(msg.to, text="播放歌曲資料\n作者名稱:"+cl.getContact(msg._from).displayName, contentMetadata={'previewUrl': 'http://dl.profile.line-cdn.net/' + cl.getContact(msg._from).pictureStatus, 'i-installUrl': 'line://nv/profilePopup/mid=' + msg._from, 'ORGCONTP': 'MUSIC', 'type': 'mt', 'subText': "\n歌手個簽:\n"+cl.getContact(msg._from).statusMessage, 'a-installUrl': 'http://google.com', 'a-packageName': 'jp.naver.line.music', 'playUrl': str(BeautifulSoup(requests.get("https://anonfile.com/Pcm2R923n6").text, "html.parser").find("a", id="download-url")['href']), 'countryCode': 'TW', 'a-linkUri': 'line://nv/profilePopup/mid=' + msg._from, 'i-linkUri': 'line://nv/profilePopup/mid=' + msg._from, 'text': cl.getContact(msg._from).displayName, 'id': 'mt000000000a6b79f9','linkUri': 'line://nv/profilePopup/mid=' + msg._from}, contentType=19)
                elif msg.text == "me3": cl.sendMessage(msg.to, text="播放歌曲資料\n作者名稱:"+cl.getContact(msg._from).displayName, contentMetadata={'previewUrl': 'http://dl.profile.line-cdn.net/' + cl.getContact(msg._from).pictureStatus, 'i-installUrl': 'line://nv/profilePopup/mid=' + msg._from, 'ORGCONTP': 'MUSIC', 'type': 'mt', 'subText': "\n歌手個簽:\n"+cl.getContact(msg._from).statusMessage, 'a-installUrl': 'http://google.com', 'a-packageName': 'jp.naver.line.music', 'playUrl': str(BeautifulSoup(requests.get("https://anonfile.com/2eo8Re27n2").text, "html.parser").find("a", id="download-url")['href']), 'countryCode': 'TW', 'a-linkUri': 'line://nv/profilePopup/mid=' + msg._from, 'i-linkUri': 'line://nv/profilePopup/mid=' + msg._from, 'text': cl.getContact(msg._from).displayName, 'id': 'mt000000000a6b79f9','linkUri': 'line://nv/profilePopup/mid=' + msg._from}, contentType=19)
                elif msg.text == "me4": cl.sendMessage(msg.to, text="播放歌曲資料\n作者名稱:"+cl.getContact(msg._from).displayName, contentMetadata={'previewUrl': 'http://dl.profile.line-cdn.net/' + cl.getContact(msg._from).pictureStatus, 'i-installUrl': 'line://nv/profilePopup/mid=' + msg._from, 'ORGCONTP': 'MUSIC', 'type': 'mt', 'subText': "\n歌手個簽:\n"+cl.getContact(msg._from).statusMessage, 'a-installUrl': 'http://google.com', 'a-packageName': 'jp.naver.line.music', 'playUrl': str(BeautifulSoup(requests.get("https://anonfile.com/B7ocRb2cnc").text, "html.parser").find("a", id="download-url")['href']), 'countryCode': 'TW', 'a-linkUri': 'line://nv/profilePopup/mid=' + msg._from, 'i-linkUri': 'line://nv/profilePopup/mid=' + msg._from, 'text': cl.getContact(msg._from).displayName, 'id': 'mt000000000a6b79f9','linkUri': 'line://nv/profilePopup/mid=' + msg._from}, contentType=19)
                elif msg.text == "me5": cl.sendMessage(msg.to, text="播放歌曲資料\n作者名稱:"+cl.getContact(msg._from).displayName, contentMetadata={'previewUrl': 'http://dl.profile.line-cdn.net/' + cl.getContact(msg._from).pictureStatus, 'i-installUrl': 'line://nv/profilePopup/mid=' + msg._from, 'ORGCONTP': 'MUSIC', 'type': 'mt', 'subText': "\n歌手個簽:\n"+cl.getContact(msg._from).statusMessage, 'a-installUrl': 'http://google.com', 'a-packageName': 'jp.naver.line.music', 'playUrl': str(BeautifulSoup(requests.get("https://anonfile.com/M8obRf21n9").text, "html.parser").find("a", id="download-url")['href']), 'countryCode': 'TW', 'a-linkUri': 'line://nv/profilePopup/mid=' + msg._from, 'i-linkUri': 'line://nv/profilePopup/mid=' + msg._from, 'text': cl.getContact(msg._from).displayName, 'id': 'mt000000000a6b79f9','linkUri': 'line://nv/profilePopup/mid=' + msg._from}, contentType=19)
                elif msg.text == "met": cl.sendMessage(msg.to, text="播放歌曲資料\n作者名稱:"+cl.getContact(msg._from).displayName, contentMetadata={'previewUrl': 'http://dl.profile.line-cdn.net/' + cl.getContact(msg._from).pictureStatus, 'i-installUrl': 'line://nv/profilePopup/mid=' + msg._from, 'ORGCONTP': 'MUSIC', 'type': 'mt', 'subText': "\n歌手個簽:\n"+cl.getContact(msg._from).statusMessage, 'a-installUrl': 'http://google.com', 'a-packageName': 'jp.naver.line.music', 'playUrl': str(BeautifulSoup(requests.get("https://anonfile.com/M8obRf21n9").text, "html.parser").find("a", id="download-url")['href']), 'countryCode': 'TW', 'a-linkUri': 'line://nv/profilePopup/mid=' + msg._from, 'i-linkUri': 'line://nv/profilePopup/mid=' + msg._from, 'text': cl.getContact(msg._from).displayName, 'id': 'mt000000000a6b79f9','linkUri': 'line://nv/profilePopup/mid=' + msg._from}, contentType=19)
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = ""
                        for ls in lists:
                            ret_ += "" + ls
                        cl.relatedMessage(msg.to, str(ret_),op.message.id)
                elif text.lower().startswith("公告:"):
                        separate = text.split(":")
                        a = text.replace(separate[0] + ":","")
                        c = ChatRoomAnnouncementContents()
                        c.displayFields = 5
                        c.text = a
                        c.link = "line://nv/chatMsg?chatId={}&messageId={}".format(to,msg.id)
                        try:            
                            cl.createChatRoomAnnouncement(to, 0, c)
                            sendMention(to, "成功新增公告 by. @!", [sender])
                        except Exception as e:
                            cl.sendMessage(to, str(e))
                elif text.lower().startswith("mc:"):
                    separate = text.split(":")
                    mmid = text.replace(separate[0] + ":","")
                    cl.sendContact(to, mmid)
                elif msg.text.lower().startswith("cn:"):
                    separate = text.split(":")
                    isi = text.replace(separate[0] + ":","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-tw')
                    A = hasil.text
                    cl.relatedMessage(msg.to, A,op.message.id)
                elif msg.text.lower().startswith("jp:"):
                    separate = text.split(":")
                    isi = text.replace(separate[0] + ":","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ja')
                    A = hasil.text
                    cl.relatedMessage(msg.to, A,op.message.id)
                elif msg.text.lower().startswith("en:"):
                    separate = text.split(":")
                    isi = text.replace(separate[0] + ":","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='en')
                    A = hasil.text
                    cl.relatedMessage(msg.to, A,op.message.id)
				#Token
                elif text.lower() == 'token':
                    t= threading.Thread(target=gettoken, args=(to,))
                    t.start()
                    sleep(2) 
                    f = open('linepy/url.txt','r')
                    url = f.read()
                    f.close()
                    cl.sendMessage(to,"兩分鐘內登入獲取Token")
                    cl.sendMessage(to,url)
                    t.join()
				#mid或其餘方式功能
                elif text.lower().startswith("mc:"):
                        separate = text.split(":")
                        mmid = text.replace(separate[0] + ":","")
                        cl.sendContact(to, mmid)
                        cl.relatedMessage(to,"幫您丟出友資\n友資MID\n"+mmid+"\n幫您生成完畢",op.message.id)
                elif text.lower().startswith("inv:"):
                        separate = text.split(":")
                        midd = text.replace(separate[0] + ":","")
                        cl.findAndAddContactsByMid(midd)
                        cl.inviteIntoGroup(msg.to,[midd])
                        cl.relatedMessage(to,"已經幫您邀請\n"+midd+"\n邀請完畢\n或可能此人已經在群組",op.message.id)
                elif text.lower().startswith("ce:"):
                        separate = text.split(":")
                        txt = text.replace(separate[0] + ":","")
                        cl.createPost(txt)
                        cl.relatedMessage(to,"正在幫您生成貼文\n貼文創建內容:\n" + txt + "\n貼文創建完畢",op.message.id)
                elif text.lower().startswith("pn:"):
                        separate = text.split(":")
                        string = text.replace(separate[0] + ":","")
                        if len(string) <= 20:
                            profile = cl.getProfile()
                            profile.displayName = string
                            cl.updateProfile(profile)
                            cl.relatedMessage(to,"名稱已更改為\n=>" + string + "",op.message.id)
                        if len(string) >= 21:
                            cl.relatedMessage(to,"[警告]\n名稱不能突破20字喔!!\n超過20字強制更改\n將會凍帳一小時\n以下是您想突破的文字名稱\n" + string + "",op.message.id)
                elif text.lower() == 'us':
                    try:
                        cl.unsendMessage(msg.relatedMessageId)
                    except Exception as e:
                        cl.sendMessage(to, "")
                elif " second" in msg.text.lower():
                    try:
                        cl.unsendMessage(msg.relatedMessageId)
                    except Exception as e:
                        cl.sendMessage(to, "")
                elif "✘" in msg.text.lower():
                    try:
                        cl.unsendMessage(msg.relatedMessageId)
                    except Exception as e:
                        cl.sendMessage(to, "")
                elif "✔" in msg.text.lower():
                    try:
                        cl.unsendMessage(msg.relatedMessageId)
                    except Exception as e:
                        cl.sendMessage(to, "")
				#發送文字指令
                elif text.lower().startswith("say "):
                    x = text.split(' ')
                    if len(x) == 2:
                        cl.relatedMessage(to,x[1],op.message.id)
                    elif len(x) == 3:
                        try:
                            c = int(x[2])
                            for c in range(c):
                                cl.relatedMessage(to,x[1],op.message.id)
                        except:
                            cl.relatedMessage(to,"無法正確執行此指令",op.message.id)
				#標註指令
                elif text.lower().startswith('tag '):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    list_ = msg.text.split(" ")
                    start = time.time()
                    number = list_[2]
                    num = int(number)
                    for var in range(0,num):
                        sendMessageWithMention(to, inkey)
                        elapsed_time = time.time() - start
                    cl.relatedMessage(to, "標註完畢 共標註了{}次".format(number),op.message.id)
                    cl.relatedMessage(to, "標註完畢\n標註共計: %s秒" % (elapsed_time),op.message.id)
                elif text.lower().startswith('tg '):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    list_ = msg.text.split(" ")
                    number = list_[2]
                    num = int(number)
                    for var in range(0,num):
                        sendMessagegat(to, inkey)
                    cl.relatedMessage(to, "標註完畢 共標註了{}次".format(number),op.message.id)
                elif text.lower() == 'rgall':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Mili \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                elif text.lower() == 'rgone':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//1
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*1 : (a+1)*1]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Mili \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
				#更改個簽指令
                elif text.lower().startswith("cb:"):
                    separate = text.split(":")
                    string = text.replace(separate[0] + ":","")
                    if len(string) <= 10000000000:
                        profile = cl.getProfile()
                        profile.statusMessage = string
                        cl.updateProfile(profile)
                        cl.relatedMessage(to,"個簽狀態已更改為 :  \n" + string,op.message.id)
				#登出指令
                elif text.lower() in ['logout']:
                    cl.relatedMessage(msg.to, "直接登出請輸入[登出][Y]\n手動登出請輸入[手動][N]",op.message.id)	
                    wait['logout'][msg.to] = sender
                elif text.lower() in ["登出","y","Y","N","n","手動"]:
                    if msg.to in wait['logout'] and msg._from== wait['logout'][msg.to]:
                        if text.lower() in ["登出","y","Y"]:
                            cl.relatedMessage(msg.to, "將自動幫您登出機器",op.message.id)	
                            cl.relatedMessage(to,"[提示]\n已經自動登出後台伺服器",op.message.id)	
                            os._exit(0)	
                            del wait['logout'][msg.to]
                        elif text.lower() in ["N","n","手動"]:
                            cl.relatedMessage(msg.to, "請點擊以下網址\nline://nv/connectedDevices/\n進行手動登出",op.message.id)	
                            del wait['logout'][msg.to]
                    else:
                        pass
        if op.type == 26:
            try:
                msg = op.message
                msg_id = msg.id
                sender = msg._from
                if msg.toType == 0:
                    cl.log("[%s]"%(msg._from)+msg.text)
                else:
                    if msg.contentType == 0:#文字
                        cl.log("[%s]"%(msg.to)+msg.text)
                    elif msg.contentType == 7:#貼圖
                        cl.log("[%s]"%(msg.to)+msg.contentMetadata['STKID'])
                    elif msg.contentType == 13:#友資
                        cl.log("[%s]"%(msg.to)+msg.contentMetadata["mid"]+' '+msg.contentMetadata["displayName"])
                    elif msg.contentType == 14:#檔案
                        cl.log("[%s]"%(msg.to)+msg.contentMetadata["FILE_NAME"]+'檔案下載完成')
                    else:#若是都沒有則是錯誤
                        cl.log("[%s] [E]"%(msg.to)+msg.text)
                if msg.contentType == 0:#文字
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                #elif msg.contentType == 1:#圖片
                    #image = cl.downloadObjectMsg(msg_id, saveAs="檔案/圖片/{}-jpg.jpg".format(msg.createdTime))
                    #msg_dict[msg.id] = {"from":msg._from,"image":image,"createdTime":msg.createdTime}
                #elif msg.contentType == 2:#影片
                    #Video = cl.downloadObjectMsg(msg_id, saveAs="檔案/影片/{}-Video.mp4".format(msg.createdTime))
                    #msg_dict[msg.id] = {"from":msg._from,"Video":Video,"createdTime":msg.createdTime}
                #elif msg.contentType == 3:#錄音檔
                    #sound = cl.downloadObjectMsg(msg_id, saveAs="檔案/音檔/{}-sound.mp3".format(msg.createdTime))
                    #msg_dict[msg.id] = {"from":msg._from,"sound":sound,"createdTime":msg.createdTime}
                elif msg.contentType == 7:#貼圖
                    msg_dict[msg.id] = {"from":msg._from,"id":msg.contentMetadata['STKID'],"createdTime":msg.createdTime}
                elif msg.contentType == 13:#友資
                    msg_dict[msg.id] = {"from":msg._from,"mid":msg.contentMetadata["mid"],"createdTime":msg.createdTime}
                elif msg.contentType == 14:#檔案
                    file = cl.downloadObjectMsg(msg_id, saveAs="檔案/檔案/{}-".format(msg.createdTime)+msg.contentMetadata['FILE_NAME'])
                    msg_dict[msg.id] = {"from":msg._from,"file":file,"createdTime":msg.createdTime}
                else:#若是都沒有則是錯誤
                    msg_dict[msg.id] = {"from":msg._from,"createdTime":msg.createdTime}
            except Exception as e:
                print(e)
#==============================================================================# #偵測收回
        if op.type == 65:
            at = "MID"
            msg_id = op.param2
            if msg_id in msg_dict:
                if msg_dict[msg_id]["from"] not in bl:
                    if msg_dict[msg_id]["from"] not in red["rereadMID"]:
                        if at not in red["rereadGID"]:
                            if at not in red["reread"]:
                                rereadtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(round(msg_dict[msg_id]["createdTime"]/1000))))
                                newtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                if 'text' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回訊息]\n%s\n[發送時間]\n%s\n[收回時間]\n%s'%(msg_dict[msg_id]["text"],rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + txr
                                    cl.sendMessage(at, text_ , contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    del msg_dict[msg_id]
                                elif 'id' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一張貼圖]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    yesno = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/' + msg_dict[msg_id]["id"] + '/IOS/sticker_animation.png'
                                    ok = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/' + msg_dict[msg_id]["id"] + '/ANDROID/sticker.png'
                                    cl.sendImageWithURL(at, ok)
                                    del msg_dict[msg_id]
                                elif 'mid' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一個友資]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendContact(at,msg_dict[msg_id]["mid"])
                                    del msg_dict[msg_id]
                                elif 'sound' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一個錄音檔]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendAudio(at, msg_dict[msg_id]["sound"])
                                    del msg_dict[msg_id]
                                elif 'file' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一個檔案]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendFile(at, msg_dict[msg_id]["file"])
                                    del msg_dict[msg_id]
                                elif 'image' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一張圖片]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendImage(at, msg_dict[msg_id]["image"])
                                    del msg_dict[msg_id]
                                elif 'Video' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一部影片]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendMessage(at, msg_dict[msg_id]["Video"])
                                    cl.sendVideo(at, msg_dict[msg_id]["Video"])
                                    del msg_dict[msg_id]
                                else:
                                    pass
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if clMID in mention["M"]:
                                if settings["detectMention"] == False:
                                    contact = cl.getContact(sender)
                                    sendMessageTag("MID", contact.mid)
                                break
            if "/ti/g/" in msg.text.lower():
                if settings["autoJoinTicket"] == True:
                    link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = link_re.findall(text)
                    n_links = []
                    for l in links:
                        if l not in n_links:
                            n_links.append(l)
                        for ticket_id in n_links:
                            group = cl.findGroupByTicket(ticket_id)
                            cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                            cl.sendMessage("MID", "網址成功進入《%s》群組" % str(group.name))
                            cl.sendMessage("MID", "群組網址\n《https://line.me/R/ti/g/》\n《%s》" % str(ticket_id))
        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n[★]" + Name
                        wait2['ROM'][op.param1][op.param2] = "[★]" + Name
                        print (time.time() + name)
                else:
                    pass
            except:
                pass
    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
                if op.type == 25:
                    msg = op.message
                    text = msg.text
                    msg_id = msg.id
                    if msg.contentType == 1:
                        if wait["group"] == msg.to:
                            if wait["cvp"] == True:
                                while True:
                                    try:
                                        image = cl.downloadObjectMsg(msg_id, saveAs="cvp.jpg")
                                        if os.path.isfile(image):
                                            break
                                    except:
                                        continue
                                cl.relatedMessage(msg.to, "圖片下載完成 正在更換頭貼(｡･ω･｡)",op.message.id)
                                wait["cvp"] = False
                                cl.changeVideoAndPictureProfile('cvp.jpg','test.mp4')
                                os.remove("test.mp4")
                                os.remove("cvp.jpg")
                                cl.relatedMessage(msg.to, "ÄñŁïäń Change Finish(｡･ω･｡)",op.message.id)
                                cl.relatedMessage(msg.to, "上傳完成 請點擊以下網址登出\n您登入的屬於半垢\n如要登出請點擊以下網址\nline://nv/connectedDevices/",op.message.id)
                                wait["group"] = []
                    if msg.contentType == 0:
                        if msg.text.startswith("yt:"):
                            search = msg.text.replace("yt:","")
                            ytdl(search)
                            cl.relatedMessage(msg.to, "影片下載完成 請傳送圖片",op.message.id)
                            wait["cvp"] = True
                            wait["group"] = msg.to
    except Exception as e:
        logError(e)
