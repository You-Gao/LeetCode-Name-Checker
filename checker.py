import urllib.request
import urllib.parse
import urllib.error
from concurrent.futures import ThreadPoolExecutor
import time

file = "4-letter-words.txt" # modify to your own file
website = "https://www.leetcode.com/"

def convertTxTtoList(file):
    with open(file) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def appendToFile(name):
    with open("output.txt", "a") as f:
        f.write(name + "\n")
    return 0

def clearOutputFile():
    with open("output.txt", "w") as f:
        f.write("")
    return 0

def checkUsernameAvailability(username):
    url = website + username
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        response = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(username + " is available")
            appendToFile(username)
        if e.code == 403:
            print("403 Forbidden")
        if e.code == 429:
            print("429 Too Many Requests")
            time.sleep(10)
    return 0

def main():
    # clear and makes the output
    clearOutputFile()
    content = convertTxTtoList(file)

    for username in content:
        checkUsernameAvailability(username)
        # sleep to slow down requests
        time.sleep(1)
    return 0

if __name__ == '__main__':
    main()