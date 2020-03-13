import matplotlib.pyplot as ppp
from numpy import *
ppp.figure(2, figsize=(8, 4))       #绘制第二张图
ppp.plot([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 8, 8, 8])
ppp.figure(1, figsize=(8, 4))
'''ppp.subplot(3, 3, 9)
ppp.subplot(3, 3, 8)'''#绘制多子图
x_values = arange(0.0, 6.0, 0.1)
y_values = sin(x_values)
ppp.title("matplotlib图形可视化")
ppp.xlabel("x")
ppp.ylabel("sin(x)")
ppp.plot(x_values, y_values, 'r--', linewidth=5.0)
ppp.grid()                  #网格
ppp.ylim(-1, 1)             #设置显示位置
ppp.xlim(0, 6)
#ppp.savefig('sin.png')         #保存到当前文件夹
#ppp.close(2)          #清空某个图
ppp.show()

#条形图
import matplotlib.pyplot as ppp
import numpy as np
#x = np.arange(9)
y = [20, 10, 30, 40, 50, 70, 60, 80, 90]
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ppp.bar(x, height=y, color='green', width=0.5)
ppp.show()