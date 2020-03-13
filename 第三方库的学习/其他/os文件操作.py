import os
#os.chdir(r'C:\Users\李佳欣\Desktop\py\wo')    #进入当前文件夹
#获取文件夹的信息
im = ''
for files in os.walk(r'C:\Users\李佳欣\Desktop\李佳欣'):
        #print(root)  # 当前目录路径
        #print(dirs)  # 当前路径下所有子目录
        print(files)  #所有文件
        for i in files:
                for ii in i:
                        im = im+ii
        print(im)

if str(os.walk('aslkjd'))[:17] == '<generator object':
        print(123)
else:
        print(555)

import os
names = os.listdir(r"D:\新建文件夹\编程资源库\爬虫")#目录下的第一级所有文件夹名字
print(names)

print(os.path.exists(r'D:\新建文件夹\编程资源库\爬虫'))#判断是否存在

#cmd使用
#os.system('calc')#cmd计算器；实在不行就用绝对位置；不能有多余空格！
#打开别的文件
#os.system("2.py")

#import os
#os.makedirs("d://1//2//3//4//5")#创建多级目录

import inspect, os
def path():
    caller_file = inspect.stack()[1][1]
    print(caller_file)
    return os.path.abspath(os.path.dirname(caller_file))
print(path())


import sys
import os
print(sys.path[0])
print(sys.argv[0])
print(os.path.dirname(os.path.realpath(sys.executable)))
print(os.path.dirname(os.path.realpath(sys.argv[0])))
