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
print("the word is=", word)
url = 'https://fanyi.baidu.com/gettts?lan=uk&text='+word+'&spd=3&source=web'
res = requests.get(url)
body = res.content
with open('tmp.mp3', 'wb') as file_obj:
    file_obj.write(body)
playsound('tmp.mp3')