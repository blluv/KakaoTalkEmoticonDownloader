import requests

dw_url = "https://item.kakaocdn.net/dw/{eid}.emot_{num:03d}.{ext}"
exts = ["png", "gif", "webp"]

def getEmoticonInfo(url):
    html = requests.get(url, headers={"User-Agent":"Android"}).text
    eid = html.split("kakaotalk://store/emoticon/")[1].split("?")[0]
    name = html.split("| ")[1].split("\"")[0]

    return (eid, name)

def getEmoticonType(eid):
    for ext in exts:
        if requests.get(dw_url.format(eid=eid, num=1, ext=ext)).status_code == 200:
            return ext
    raise Exception("Unknown Type")

def getEmoticonUrl(eid, etype, num):
    return dw_url.format(eid=eid, ext=etype, num=num)
