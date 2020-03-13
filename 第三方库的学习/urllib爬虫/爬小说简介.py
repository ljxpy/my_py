#爬虫学习
import time
from urllib import request
from bs4 import BeautifulSoup
for i in range(792000, 793085):
    f = request.urlopen(r"http://book.zongheng.com/book/{}.html".format(i))
    f = f.read()
    f = f.decode('utf-8')
    soup = BeautifulSoup(f, 'html.parser')
    es1 = soup.find_all(attrs={"class": "book-dec Jbook-dec hide"})#attrs={"class": "topicText"}
    es1 = str(es1)
    baocu = ""
    cc = 0
    for i in range(len(es1)-2):
        c = es1[i:i+3]
        if c == "<p>":
            cc = 1
        if c == r"</p":
            cc = 0
        if cc == 1:
            baocu = baocu+es1[i]
    es2 = soup.find_all(attrs={"class": "book-name"})
    es2 = str(es2)
    es2c = 0
    sm = ""
    es2cc = ""
    for i in range(len(es2)):
        es2cc = es2[i]
        if es2c == 1:
            sm = sm+es2[i]
        if es2cc ==">":
            es2c = 1
        if i == "\000":
            es2c = 0
    print("书名：",sm[:15])
    print("简介：", baocu[3:])
    print()

