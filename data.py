import urllib.request as request
import json

src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

with request.urlopen(src) as response:
  data = json.load(response)  #利用json模組處理json資料格式
  glist = data["result"]["results"]

for place in glist:
    if int(place["xpostDate"][:4]) >= 2015:
         print(place["stitle"] + ',' + place["longitude"] + ',' +
            place["latitude"] + ','+'https://' +"place['file'].split('.jpg')[0]".lower()+'.jpg')