import numpy as np
import matplotlib.pyplot as plt
# 分成32*32的图片，3个通道
A = np.random.randn(3072).reshape(32,32,3)
A = np.maximum(A,0)
#显示出来
plt.imshow(A)
plt.show()
