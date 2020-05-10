import requests
import json
import time

url = "https://codeforces.com/ratings/all/true/page/"

with open("handles.json", "r") as handlesjson:
    handles = json.load(handlesjson)

tot = 0
page = 425

while tot < 10000:
    page += 1
    while True:
        try:
            s = requests.get(url + str(page)).text
        except:
            print("Try again...")
            time.sleep(1)
        else:
            break
    p = s.find("outdated")
    while p != -1 and tot < 1000:
        nxt = s.find("outdated", p + 1)
        sta = s.find("/profile/", p)
        end = s.find("\"", sta)
        handle = s[sta + 9:end]
        handles.append(handle)
        tot += 1
        print(handle)
        p = nxt

f = open("handles.json", "w")
f.write(json.dumps(handles))
