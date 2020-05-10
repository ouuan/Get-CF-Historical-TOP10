import json
import time
import operator
import datetime

maxPerDay = 100

with open("handles.json", "r") as handlesjson:
    handles = json.load(handlesjson)

with open("data.json") as datajson:
    data = json.load(datajson)

with open("countries.json") as countriesjson:
    countries = json.load(countriesjson)

STARTTIME = datetime.datetime(2010, 2, 19)

f = open("data.csv", "w")

f.write("name,type,value,date\n")

old = []

for i in range(len(data["tourist"])):
    temp = []
    tim = (STARTTIME + datetime.timedelta(days=i)).strftime("%Y/%m/%d")
    for j in handles:
        temp.append({"handle": j, "rating": data[j][i]})
    temp.sort(key=lambda x: x["rating"], reverse=True)
    if operator.eq(temp[:maxPerDay], old[:maxPerDay]):
        continue
    for j in range(maxPerDay):
        u = temp[j]
        f.write(u["handle"] + "," + countries[u["handle"]] + "," +
                str(u["rating"]) + "," + tim + "\n")
    old = temp
