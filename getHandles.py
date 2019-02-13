import requests
import json
import time

url="https://codeforces.com/ratings/page/"

headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "referer": "https://codeforces.com/"
}

handles=[]

for page in range(1,26):
    while True:
        try:
            s=requests.get(url+str(page),headers=headers).text
        except:
            print("failed")
            time.sleep(1)
        else:
            print("success")
            break
    p=s.find("text-align:left;padding-left:1em;")
    while p!=-1:
        nxt=s.find("text-align:left;padding-left:1em;",p+1)
        sta=s.find("/profile/",p)
        end=s.find("\"",sta)
        handle=s[sta+9:end]
        handles.append(handle)
        print(handle)
        p=nxt

f=open("handles.json","w")
f.write(json.dumps(handles))
