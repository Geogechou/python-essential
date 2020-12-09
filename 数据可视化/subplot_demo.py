import matplotlib.pyplot as plt
index = [1,2,3,4,5]
g_loss = [1.0,2.0,3.0,2.0,1.0]
d_loss = [5.0,4.0,3.0,2.0,1.0]
plt.figure()
# 划分整张图为,垂直2个，水平1个
# 呈以下的形状
'''
      figure
      figure
'''
# 总共2个位置，占据第一个
plt.subplot(2,1,1)
plt.plot(index,g_loss)
# 占据第二个位置
plt.subplot(2,1,2)
plt.plot(index,d_loss)
# 全部显示
plt.show()
