from urllib import request, parse
from bs4 import BeautifulSoup
from fake_useragent import UserAgent  #浏览器信息
import time
import threading
ua = UserAgent()
def gouzao():
    x = open(r"C:\Users\李佳欣\Desktop\小说网址.txt", "a")
    x.write("关键字")
    x.write("\n")
gouzao()
#get请求：爬取百度搜素
def paqubaocun(y):
    headers = {
    'User-Agent': ua.random,
    "Referer":"http://www.zongheng.com/",
    'Accept-Language': 'zh-CN',
    #'Cookie': 'kg_dfid=4Djydx1uwQK70dKy9Z1onluO; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1582364360,1582367099,1582367478,1582424228; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; kg_mid=3d87f0e68527090d7f2b6b71c9cd5e37; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1582424256',

    }
    data1 = {
    'keyword':y,
    }
    data = parse.urlencode(data1)
    url = r"http://search.zongheng.com/s?{}".format(data)
    print(url)
    req = request.Request(url=url, headers=headers)
    f1 = request.urlopen(req, timeout=5)
    f = f1.read()
    f = f.decode("utf-8")
    def zhongwen(x):
        if '\u4e00' <=x and x <= '\u9fff':
            return True
    def cun(qqq):
        x = open(r"C:\Users\李佳欣\Desktop\小说网址.txt", "a")
        x.write(qqq)
        x.write("\n")
    def cishu(x,y):
        cs = 0
        for i in range(len(x)):
            if y == x[i]:
                cs = cs+1
        return cs
    esstr = ""
    esstr = esstr + f
    #c4 = [1,2,3]
    for i in range(len(esstr)):
        c = esstr[i:i+7]
        if c == r"http://"and esstr[i+36:i+41] == ".html":#and cishu(c4, esstr[i+41-11:i+41-5]) == 2
            c1 = esstr[i:i+41]
            c2 = []
            for ii in range(i+52, i+200):
                if zhongwen(esstr[ii]):
                    c2.append(esstr[ii])
            c3 = ""
            for iii in range(len(c2)):
                c3 = c3+c2[iii]
            #c4.append(esstr[i+41-11:i+41-5])
            #del c4[0]
            c5 = c3+c1
            if c5[0:4] == "书籍详情"or c5[0:4] == "http"or c5[0:4] == "友情链接":
                continue
            else:
                cun(c5)
                print(c5)

x = ["学习，见谅。求放过"]
for i in range(len(x)):
    t = threading.Thread(target=paqubaocun, args=(x[i],))
    t.start()