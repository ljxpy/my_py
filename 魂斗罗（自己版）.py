#1.落地有时会粘住不能左右走动，因为luoditiao()越界
import pygame
from pygame.locals import *
import sys
import time
class jinlinlei():
    t =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    n = 19                 #图片的个数
    j = 0
    s1 = [0, 0]
    jinlinbiao = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    jinlinbiao2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    def zairuduozhang(self):
        print("加载图片中---")
        for i in range(self.n):
            t = pygame.image.load('%d.jpg' % (i + 1))
            self.jinlinbiao[i] = t
            self.jinlinbiao2[i] = t.get_rect()
            print("加载精灵%d图片完成" % i)
            if i+1 == self.n:
                print("精灵共%d张图片加载完成" % self.n)
    def xianshiduozhang(self):
        if self.s1[0] % 1 == 0:
            py.blit(self.jinlinbiao[self.s1[0]], self.jinlinbiao2[self.s1[0]])
        else:
            py.blit(self.jinlinbiao[int(self.s1[0])], self.jinlinbiao2[int(self.s1[0])])
        self.s1[0] = self.s1[0] + 0.1      #修改类属性实现动画得快慢
        if self.s1[0] == self.n:
            self.s1[0] = 0

    def zairuyizhang(self):
        print("启用加载单个精灵图片方法")
        self.j = pygame.image.load('D:\\新建文件夹\\python\\projec'
                              't3.5\\初步练习\\3平时的小写作\\《'
                              '魂斗罗第一关》自己版\\魂斗罗图片\\anzhuo.gif')
        jweizhi = self.j.get_rect()
        for i in range(11):
            h1 = pygame.Rect(jweizhi.width//11*i, 0, jweizhi.width//11, 80)
            h2 = self.j.subsurface(h1)
            self.t[i] = h2
    def xianshiyizhang(self):
        py.blit(self.t[int(self.s1[1])], (920, 10))
        self.s1[1] = self.s1[1] + 0.1
        if int(self.s1[1]) == 11:
            self.s1[1] = 0
class zidanlei():
    __s = 0
    __zidan3 = 0
    __fangxiang2 = 0
    def fx(self,__fangxiang2):
        if __fangxiang2 == 3:
            return (10, 0)
        elif __fangxiang2 == 1:
            return (-10, 0)
        elif __fangxiang2 == 5:
            return (10, 0)     #（0，-10）修改过
        elif __fangxiang2 == 2:
            return (10, 0)      #（0，10）修改过
    def zidan(self):
        global zidan1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                zidanlei.__fangxiang2 = fangxiangad
                zidanlei.__s = 1
                zidanlei.__zidan3 = tanke2.move(130, 30)
        if zidanlei.__s == 1:
            zidanlei.__zidan3 = zidanlei.__zidan3.move(zidanlei.fx(self, zidanlei.__fangxiang2))
            py.blit(zidan1, zidanlei.__zidan3)
            if zidanlei.__zidan3.left <= 0 or zidanlei.__zidan3.right >= 1200 \
                or zidanlei.__zidan3.top <= 0 or zidanlei.__zidan3.bottom >= 500:
                zidanlei.__s = 0
def ludikz(movec):
    global beijin2, tankesudu, ditujs, tanke2, fangxiangws,fangxiangad
    yx1x2liebiao = ditu().ludic   #当背景移动时，修改参数
    print(yx1x2liebiao)           #提示作用
    if yx1x2liebiao[0]-tanke2.bottom >= 0 and\
       tanke2.right >= yx1x2liebiao[1] and\
            tanke2.left <= yx1x2liebiao[2]:
        if movec == (0, tankesudu):
            tanke2 = tanke2.move(movec)
            fangxiangws = 2
            if yx1x2liebiao[0] - tanke2.bottom < 0:
                tanke2 = tanke2.move((0, -tankesudu))
                print("陆地控制低于地面反弹")
        elif movec == (tankesudu, 0):
            beijin2 = beijin2.move(-tankesudu, 0)
            fangxiangad = 3
            ditujs = ditujs + tankesudu
        elif movec == (-tankesudu, 0):
            beijin2 = beijin2.move(tankesudu, 0)
            fangxiangad = 1
            ditujs = ditujs - tankesudu
        elif movec == (0, -tankesudu):
            tanke2 = tanke2.move(movec)
            fangxiangws = 5
    else:
        tanke2 = tanke2.move((0, -tankesudu))
        print("陆地控制不在范围内进行反弹")
def luoditiao():
    global upc, upt, tanke2, tankesudu, tbl,upcc
    if upc == 1:
        upt = upt + 1
        if upt < 30:
            upcc = 0
            tbl = 0
            movec = (0, -tankesudu)
            ludikz(movec)#改
        else:
            upt = 0
            upc = -1
            tbl = 0
    if upc == -1:
        upt = upt + 1
        if upt < 30:
            tbl = 0
            movec = (0, tankesudu)
            ludikz(movec)
        else:
            upt = 0
            upc = 0
            tbl = 1
            upcc = 1
def gaojiyidong():
    global leftc, rightc, downc, tankesudu
    luoditiao()
    if event.type == pygame.KEYUP:
        if (event.key == pygame.K_LEFT):
            leftc = 0
        if (event.key == pygame.K_RIGHT):
            rightc = 0
        if (event.key == pygame.K_DOWN):
            downc = 0
    if leftc == 1and ditug == 1:
        movec = (-tankesudu, 0)
        ludikz(movec)
    if rightc == 1and ditug == 1:
        movec = (tankesudu, 0)
        ludikz(movec)
    if downc == 1and ditug == 1 and tbl == 1:
        movec = (0, tankesudu)
        ludikz(movec)
class ditu():
    ditu_ludi = [[300, 0, 220], [250, 0, 560], [300, 0, 100], [300, 0, 170], [300, 0, 100],
                 [300, 0, 1500]]
    ludic = [0, 0, 0]
    def dituyidong(self):
        global ditujs, dituaa, ditug, tanke2, fangxiangws,fangxiangad, ditu1
        if abs(self.ludic[2] - ditujs) < 1 and fangxiangad == 3 or ditu1 == 1:
            print("向前切换")
            dituaa = dituaa + 1
            self.ludic[0] = self.ditu_ludi[dituaa][0]
            self.ludic[1] = self.ditu_ludi[dituaa][1]
            self.ludic[2] = self.ditu_ludi[dituaa][2]
            ditujs = 0
            ditu1 = 0
        '''if abs(self.ludic[2] - ditujs) < 1 and fangxiangad == 1:
            print("向后切换")
            self.ludic[0] = self.ditu_ludi[dituaa][0]
            self.ludic[1] = self.ditu_ludi[dituaa][1]
            self.ludic[2] = self.ditu_ludi[dituaa][2]
            ditujs = self.ditu_ludi[dituaa][2]'''
def gaoyuludi():
    global tanke2, ditug
    if tanke2.bottom <= ditu().ludic[0]:
        print("高于陆地恢复")
        ditug = 1
    if tanke2.bottom > ditu().ludic[0]and ditug == 1:
        print("低于陆地太低自锁")
        ditug = 0
        ludikz((0, -tankesudu))
class huairen():
    def __init__(self):
        pass
    def bin_pao(self):
        global binpao_weizhi, binpaoc
        if binpaoc == 1:
            binpao_weizhi = binpao_weizhi.move(-5, 0)
            if rightc == 1:
                binpao_weizhi = binpao_weizhi.move(-5, 0)
            if binpao_weizhi.right < 0:
                binpaoc = 0
            if (binpao_weizhi.bottom+binpao_weizhi.top)/2 <= tanke2.bottom \
                    and(binpao_weizhi.bottom+binpao_weizhi.top)/2 >= tanke2.top \
                    and binpao_weizhi.left <= tanke2.right:
                print("you，die")
#主函数
pygame.init()
pygame.mixer.init()
py = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("魂斗罗（李佳欣版）")
        #参数
tupian1 = ('D:\\新建文件夹\\python\\projec'
           't3.5\\初步练习\\3平时的小写作\\《'
           '魂斗罗第一关》自己版\\魂斗罗图片\\1.jpg')
tupian2 = ('D:\\新建文件夹\\python\\projec'
           't3.5\\初步练习\\3平时的小写作\\《'
           '魂斗罗第一关》自己版\\魂斗罗本人\\前.gif')
tupian3 = ('D:\\新建文件夹\\python\\projec'
           't3.5\\初步练习\\3平时的小写作\\《'
           '魂斗罗第一关》自己版\\魂斗罗本人\\zidan.gif')
tupian4 = ('D:\\新建文件夹\\python\\projec'
           't3.5\\初步练习\\3平时的小写作\\《'
           '魂斗罗第一关》自己版\\带枪小兵\\后跑.png')
yinxiao1 = ('D:\\新建文件夹\\python\\projec'
           't3.5\\初步练习\\3平时的小写作\\《'
           '魂斗罗第一关》自己版\\魂斗罗音效\\魂斗罗进行时.mp3')
sleept = 0.01
yingliang = 0.5
tankesudu = 5
fangxiangws = 3
fangxiangad = 5

#中间变量
upt = 0
upcc = 1        #跳跃的时候不允许继续跳
kongzhic = 0
upc = 0
leftc = 0
rightc = 0
downc = 0
ditujs = 0          #地图计数
dituaa = -1          #地图向前递进
ditug = 1           #高于地图才能继续前
tbl = 1             #跳的时候不能按下键位
ditu1 = 1           #第一次赋值dituc
binpaoc = 1
        #图片加载
beijin1 = pygame.image.load(tupian1)
beijin2 = beijin1.get_rect()
tanke1 = pygame.image.load(tupian2)
tanke2 = tanke1.get_rect()
zidan1 = pygame.image.load(tupian3)
binpao = pygame.image.load(tupian4)
binpao_weizhi = binpao.get_rect()
        #位置初始化
tanke2 = tanke2.move(100, 50)
binpao_weizhi = binpao_weizhi.move(1000, 170)
        #精灵
jinlinlei().zairuyizhang()

        #音效
pygame.mixer.music.load(yinxiao1)
pygame.mixer.music.set_volume(yingliang)
pygame.mixer.music.play(-1, 0)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()
    #人物移动
    if event.type == pygame.KEYDOWN:
        if (event.key == pygame.K_DOWN)and tanke2.bottom < 490:
            downc = 1
        if (event.key == pygame.K_UP) and tanke2.top > 10 and upcc == 1:
            upc = 1
        if (event.key == pygame.K_LEFT) and (tanke2.left > 10):
            leftc = 1
        if (event.key == pygame.K_RIGHT) and (tanke2.right < 990):
            rightc = 1
    ditu().dituyidong()
    gaojiyidong()
    gaoyuludi()
    #小兵的控制
    huairen().bin_pao()
    #显示
    py.blit(beijin1, beijin2)       #背景地图
    py.blit(tanke1, tanke2)         #魂斗罗本人
    zidanlei().zidan()              #子弹
    jinlinlei().xianshiyizhang()
    py.blit(binpao, binpao_weizhi)  #跑着的小兵
    pygame.display.update()         #更新地图显示
    time.sleep(sleept)