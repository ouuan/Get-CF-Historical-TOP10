import requests
import json
import time

url = "https://codeforces.com/ratings/page/"

handles = []

for page in range(1, 51):
    while True:
        try:
            s = requests.get(url + str(page)).text
        except:
            print("Try again...")
            time.sleep(1)
        else:
            break
    p = s.find("text-align:left;padding-left:1em;")
    while p != -1:
        nxt = s.find("text-align:left;padding-left:1em;", p + 1)
        sta = s.find("/profile/", p)
        end = s.find("\"", sta)
        handle = s[sta + 9:end]
        handles.append(handle)
        print(handle)
        p = nxt

f = open("handles.json", "w")
f.write(json.dumps(handles))
