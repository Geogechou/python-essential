#encoding=utf-8
import os
from matplotlib import pyplot as plt
from wordcloud import WordCloud
freq={'电磁场与微波':0.8,'通信系统':0.7,'自动控制原理':0.5,'数字信号处理':0.4,'计算机网络':0.3,'操作系统':0.3,'计算机组成':0.3,'物联网':0.1
}
font = r'C:\Windows\Fonts\simfang.TTF'
wc=WordCloud(font_path=font,
background_color='white',
width=1000,
height=1000,
max_font_size=400
).generate_from_frequencies(freq)
plt.imshow(wc,interpolation='bilinear')
plt.axis("off")
plt.savefig('test.png',ppi=500)
plt.show()
os.system("pause")