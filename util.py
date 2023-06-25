import requests

image_url = "https://item.kakaocdn.net/dw/{eid}.emot_{num:03d}.{ext}"
pack_url = "http://item.kakaocdn.net/dw/{eid}.file_pack.zip"

decrypt_required_exts = [".gif", ".webp"]
no_decrypt_required_exts = [".png"]

def getEmoticonInfo(url):
    html = requests.get(url, headers={"User-Agent":"Android"}).content.decode()
    eid = html.split("kakaotalk://store/emoticon/")[1].split("?")[0]
    name = html.split("<title>")[1].split("</title>")[0]

    return (eid, name)

def is_decrypt_required(ext):
    if ext in decrypt_required_exts:
        return True
    
    if ext in no_decrypt_required_exts:
        return False
        
    raise Exception("Unknown Type")

def getEmoticonImageUrl(eid, etype, num):
    return image_url.format(eid=eid, ext=etype, num=num)
    
def getEmoticonPackUrl(eid):
    return pack_url.format(eid=eid)
