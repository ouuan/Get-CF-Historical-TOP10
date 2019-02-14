import requests
import json
import time

with open("handles.json","r") as handlesjson:
    handles=json.load(handlesjson)

countries={}

url="https://codeforces.com/api/user.info?handles="
flag=False
for i in range(len(handles)):
    if flag:
        url=url+";"
    else:
        flag=True
    url=url+handles[i]
    if i%100==99:
        while True:
            try:
                response=requests.get(url)
            except:
                time.sleep(1)
            else:
                break;
        data=json.loads(response.text)
        for j in data["result"]:
            print(j["handle"])
            if "country" in j.keys():
                countries[j["handle"]]=j["country"]
            else:
                countries[j["handle"]]="Unknown"
        url="https://codeforces.com/api/user.info?handles="

if len(handles)%100!=0:
    while True:
            try:
                response=requests.get(url)
            except:
                print("failed")
                time.sleep(1)
            else:
                print("success")
                break;
    data=json.loads(response.text)
    for j in data["result"]:
        print(j["handle"])
        if "country" in j.keys():
            countries[j["handle"]]=j["country"]
        else:
            countries[j["handle"]]="Unknown"
    url="https://codeforces.com/api/user.info?handles="

with open("countries.json","w") as countriesjson:
    countriesjson.write(json.dumps(countries))
