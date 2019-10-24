import matplotlib.pyplot as plt
import numpy as np 
x=np.arange(-100,100,1)
## sinh function
y=np.sinh(x)
plt.figure(1)
plt.subplot(211)
plt.plot(x,y)
plt.title("sinh x")
## cosh function
print(np.cosh(0))
y_cosh=np.cosh(x)
plt.subplot(212)
#plt.subplots_adjust(top=1.2)
plt.plot(x,y_cosh)
plt.title("cosh function")
plt.show()