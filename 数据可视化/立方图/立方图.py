import matplotlib.pyplot as plt
"""
立方图demo

"""
data={'2012':3240,'2013':3883,'2014':4300,'2015':4860,'2016':5400,'2017':6480,'2018':7452}

names=list(data.keys())
values=list(data.values())
# 传入两个列表即可
fig=plt.bar(names,values,width=0.45,color='orange')
plt.title("Gross output value of China's security industry")
plt.xlabel('year')
plt.ylabel('100 minllion yuan')
#savefig()在show之前调用，不然图片信息会丢失
plt.savefig('test.jpg')
plt.show()

