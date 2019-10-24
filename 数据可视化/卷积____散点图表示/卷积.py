import numpy as np
import scipy.signal
import matplotlib.pyplot as plt


x=np.array([1,1,1])
y=np.array([1,1,1])
z=scipy.signal.convolve(x,y)

#x_label=np.array([i for i in range(len(z))])
x_label=np.array([-2,-1,0,1,2])
print(x_label)
baseline=plt.stem(x_label,z,'-.')
plt.setp(baseline,color='r',linewidth=2)
plt.savefig('conver.png')
plt.show()

