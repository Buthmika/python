import matplotlib.pyplot as plt
# y=[10,22,38,41]
# plt.plot(y)
# # plt.show()
# x2=[1,2,3,4]
# y2=[1,4,9,16]
# plt.scatter(x2,y2)
# plt.show()
import numpy as np
# x=np.arange(0,100,2)
# y1=x*2+3
# y2=np.power(x,2)
# plt.plot(x,y1,'r--',label='x vs y1')
# plt.plot(x,y2,'g+',label='x vs y2')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.savefig('newImage.png')
# plt.show()
names=['group A','group B','group C']
values=[1,10,100]
plt.figure(figsize=(12,5))
plt.subplot(133)
plt.bar(names,values)
plt.subplot(132)
plt.scatter(names,values)
plt.subplot(131)
plt.bar(names,values)

plt.suptitle('Category Plotting')
plt.savefig('test.png')
plt.show()