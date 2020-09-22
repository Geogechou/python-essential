import requests
import time
import json
timestamp = str(int(time.time()*1000))
token = requests.get("http://ehall.scu.edu.cn/yjsxkapp/sys/xsxkapp/login/4/vcode.do?timestamp="+timestamp)
jsonData =json.loads(token.text)
token =  jsonData["data"]["token"]
header = {"Content-Type":"image/jpeg"}
# 加上referer
header["Referer"]="http://ehall.scu.edu.cn/yjsxkapp/sys/xsxkapp/index.html"
rawStrings = "route=6b481a92fa88ef3f33eea32b0ae474e5; EMAP_LANG=zh; amp.locale=undefined; JSESSIONID=LQSZ1LEhaInRaZ6INmYroa7U1U2w5TKNYiuWMhmF-79_kmuKqWp2!-1329957459; amlbcookie=02; AMAuthCookie=AQIC5wM2LY4Sfcxqut58U%2F0O1T%2FhSRapg19dHeOcPQd4dqg%3D%40AAJTSQACMDI%3D%23"
cookie = {}
res = rawStrings.split(";")
for item in res:
    array = item.split("=")
    cookie[array[0]]=array[1]
url = "http://ehall.scu.edu.cn/yjsxkapp/sys/xsxkapp/login/vcode/image.do?vtoken="+token
r = requests.get(url,headers=header,cookies=cookie)
print(r.status_code)
with open("/home/george/char/test.jpg","wb") as f:
    f.write(r.content)
    f.close()
    print("write over")
