# 命令行英文朗读
import requests
from playsound import playsound
import sys
if len(sys.argv) < 2:
    word = "Please enter a word"
else:
    i = 1
    word = ""
    while i < len(sys.argv):
        word += sys.argv[i]+" "
        i += 1
print("the word is: ", word)
url = 'https://fanyi.baidu.com/gettts?lan=uk&text='+word+'&spd=3&source=web'
session = requests.Session()
# 绕过系统代理
session.trust_env = False
res = session.get(url)
body = res.content
with open('/tmp/audio.mp3', 'wb') as file_obj:
    file_obj.write(body)
playsound('/tmp/audio.mp3')
