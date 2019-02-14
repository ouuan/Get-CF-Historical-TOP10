import requests
import json
import time
import datetime

STARTTIME=datetime.datetime(2010,2,19)

def getDay(x):
    xTime=time.strftime("%Y %m %d",time.localtime(x)).split()
    xTime=datetime.datetime(int(xTime[0]),int(xTime[1]),int(xTime[2]))
    return (xTime-STARTTIME).days

NOW=getDay(time.time())

with open("handles.json","r") as handlesjson:
    handles=json.load(handlesjson)

data={}

for i in handles:
    print(i)
    while True:
        try:
            response=requests.get("https://codeforces.com/api/user.rating?handle="+i)
            userdata=json.loads(response.text)["result"]
        except:
            time.sleep(1)
        else:
            break
    old=0
    data.setdefault(i,[])
    for j in userdata:
        now=getDay(j["ratingUpdateTimeSeconds"])
        if now>=0:
            rating=j["oldRating"]
            for k in range (old,now):
                data[i].append(rating)
            old=now
    rating=userdata[-1]["newRating"]
    for k in range(old,NOW+1):
        data[i].append(rating)

with open("data.json","w") as datajson:
    datajson.write(json.dumps(data))
