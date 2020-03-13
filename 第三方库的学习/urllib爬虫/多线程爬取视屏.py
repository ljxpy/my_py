import threading
import time
from urllib import request
import socket
import os
socket.setdefaulttimeout(5)
class yi_pi():
    def __init__(self, wenjian):
        global nono
        self.wenjian = wenjian
        self.xc = []
        self.no1 = []
        self.js = 0

    def lianjie(self, url1, i):
        if i > 99:
            url = url1+str(i)+".ts"
        elif i > 9:
            url = url1+"0"+str(i)+".ts"
        else:
            url = url1+"00"+str(i)+".ts"
        return url

    def baocun(self, name, hao):
        print("线程%d开始" % name)
        # n = 1
        for i in range(n):
            try:
                print("线程%d第%d次请求" % (name, i+1))
                request.urlretrieve(self.lianjie(url1, name), r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\%d--%d\%s.ts' % (hao*200-199, hao*200,name))
                self.no1.remove(name)
                print("线程%d完成任务" % name)
                break
            except:
                if i != n-1:
                    continue
                print("！！！！！线程%d异常结束！！！！！！" % name)

    def zhu200(self, renwu, hao):
        for name in renwu:
            self.no1.append(name)
            self.xc.append(threading.Thread(target=self.baocun, args=(name, hao,)))
            #xc[name].setDaemon(True)           #守护线程
            self.xc[self.js].start()
            self.js = self.js + 1
        for t in self.xc:
            t.join()
        print("未完成的列表:", self.no1 )
    def zhu(self):
        global nono
        for i in range(1, 10):
            if 200 * i <= len(self.wenjian):
                try:
                    os.makedirs(r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\%s--%s' %(i*200-199,i*200))
                    renwu = range(i*200-199, i*200+1)
                    self.zhu200(renwu=renwu, hao=i)
                except:
                    print('建立目录重复，跳过')
            else:
                try:
                    os.makedirs(r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\%s--%s' %(i*200-199,i*200))
                    renwu = range(i * 200 - 199, len(self.wenjian)+1)
                    self.zhu200(renwu=renwu, hao=i)
                    nono = self.no1
                except:
                    print('建立目录重复，跳过')
                break

nono = []
os.makedirs(r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\%s--%s'%(0*200-199,0*200))
n = 5
url1 = 'https://v3.yongjiujiexi.com/20190502/AoGl7zOU/800kb/hls/Q05bqSXk6997'
x = range(1600)
yi_pi(x).zhu()
print(nono)
for i in range(1, 100):
    if len(nono) != 0:
        no2 = nono
        nono = []
        print('正在第%s次修复'%i)
        yi_pi(0).zhu200(no2, 0)
        print('%s次修复依旧未完成列表：'%i, nono)
    else:
        break

def zhuanyi():
    print('正在执行转移函数')
    import shutil
    images = []
    for root, dirs, files in os.walk(r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\%s--%s'%(0*200-199,0*200)):
        images = files
    print(images)
    for i in images:
        x = int(i[:-3])
        if x>0 and x<=200:
            shutil.copy(r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\%s--%s\i'%(0*200-199,0*200),
                        r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\1--200\i')
        elif x>200 and x<=400:
            shutil.copy(r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\%s--%s\i' % (0 * 200 - 199, 0 * 200),
                        r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\201--400\i')
        elif x>400 and x<=600:
            shutil.copy(r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\%s--%s\i' % (0 * 200 - 199, 0 * 200),
                        r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\401--600\i')
        elif x>600 and x<=800:
            shutil.copy(r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\%s--%s\i' % (0 * 200 - 199, 0 * 200),
                        r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\601--800\i')
        elif x>800 and x<=1000:
            shutil.copy(r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\%s--%s\i' % (0 * 200 - 199, 0 * 200),
                        r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\801--1000\i')
        elif x>1000 and x<=1200:
            shutil.copy(r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\%s--%s\i' % (0 * 200 - 199, 0 * 200),
                        r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\1001--1200\i')
        elif x>1200 and x<=1400:
            shutil.copy(r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\%s--%s\i' % (0 * 200 - 199, 0 * 200),
                        r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\1201--1400\i')
        elif x>1400 and x<=1600:
            shutil.copy(r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\%s--%s\i' % (0 * 200 - 199, 0 * 200),
                        r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\1401--1600\i')
        elif x>1600 and x<=1800:
            shutil.copy(r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\%s--%s\i' % (0 * 200 - 199, 0 * 200),
                        r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\1601--1800\i')
        elif x>1800 and x<=2000:
            shutil.copy(r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\%s--%s\i' % (0 * 200 - 199, 0 * 200),
                        r'D:\新建文件夹\编程资源库\爬虫\mov\速度与激情2\1801--2000\i')
zhuanyi()
print('最终未完成:', nono)
print('进程结束')