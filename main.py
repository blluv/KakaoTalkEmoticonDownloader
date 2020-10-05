import requests
import decrypt
import util
import os

url=input("URL: ")
eid, ename = util.getEmoticonInfo(url)
etype = util.getEmoticonType(eid)

print("EmoticonId: {}\nEmoticonName: {}\nEmoticonType: {}".format(eid, ename, etype))

i = 1
while True:
    res = requests.get(util.getEmoticonUrl(eid, etype, i))
    if res.status_code != 200:
        if res.status_code == 404:
            print("END")
        else:
            print("{} ERROR".format(res.status_code))
        break
    
    if not os.path.exists(eid):
        os.makedirs(eid)
        
    filename = "{}/{:03d}.{}".format(eid, i, etype)
    with open(filename, "wb") as f:
        f.write(decrypt.xorData(res.content))
    print("{} COMPLERE".format(filename))
    i+=1