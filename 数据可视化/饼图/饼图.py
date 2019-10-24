import matplotlib.pyplot as plt
# 以下三行使matplotlib支持中文
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

labels = ['安防', '广告营销', '解决方案', '互联网娱乐','云服务','其他']
sizes = [68, 18, 4, 4,3,3]
ax1=plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("2017年中国计算机视觉行业市场构成")
plt.savefig('pie.png')
plt.show()