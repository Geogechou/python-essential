"""
绘制散点图，本例中点数比较多，看起来像是一条连续的图
"""
import matplotlib.pyplot as plt  

x_value=range(1,1000)
y_value=[x**2 for x in x_value]
# s参数，设定点的大小,edgecolor是轮廓 
#指定渐变颜色
#plt.scatter(x_value,y_value,s=1,edgecolor='none',c=y_value,cmap=plt.cm.Reds)
plt.scatter(x_value,y_value,s=1,edgecolor='none',c=y_value)
plt.title("square number",fontsize=20)
plt.xlabel("value",fontsize=10)
plt.ylabel("square of value",fontsize=10)
# y坐标轴旋转45度
plt.yticks(rotation=45)
plt.tick_params(axis='both',labelsize=14)
# 设置坐标轴的取值范围
plt.axis([0,1100,0,1100000])
plt.savefig('squares_plot.png',bbox_inches='tight')
plt.show()

