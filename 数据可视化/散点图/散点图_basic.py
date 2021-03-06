"""
最简单的散点图
"""
import matplotlib.pyplot as plt 
x_values=[1,2,3,4,5]
y_values=[1,4,9,16,25]
plt.scatter(x_values,y_values,s=20)
# 设置图标标题并给坐标轴加上标签
plt.title("Square number",fontsize=24)
plt.xlabel("Value",fontsize=14) 
plt.ylabel("Square of Value",fontsize=14)
# 显示刻度标记的大小
plt.tick_params(axis='both',labelsize=14)
plt.show()
