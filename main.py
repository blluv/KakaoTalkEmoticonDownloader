import requests
import zipfile
import decrypt
import util
import os
import io

url=input("URL: ")

eid, ename = util.getEmoticonInfo(url)
print("EmoticonId: {}\nEmoticonName: {}".format(eid, ename))

res = requests.get(util.getEmoticonPackUrl(eid))
if res.status_code != 200:
    print("{} ERROR".format(res.status_code))
    os.exit(1)
    
if not os.path.exists(eid):
    os.makedirs(eid)
    
with zipfile.ZipFile(io.BytesIO(res.content), "r") as zf:
    namelist = zf.namelist()
    for idx, filepath in enumerate(namelist):
        _, ext = os.path.splitext(filepath)

        if util.is_decrypt_required(ext):
            emot = decrypt.xorData(zf.read(filepath))
        else:
            emot = zf.read(filepath)
            
        filename = "{}/{}".format(eid, os.path.basename(filepath))
        
        with open(filename, "wb") as f:
            f.write(emot)
            
        print("success {}/{}".format(idx+1, len(namelist)))
