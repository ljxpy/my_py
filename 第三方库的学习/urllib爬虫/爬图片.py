from urllib import request
from bs4 import BeautifulSoup
f1 = "https://www.enterdesk.com/special/wmtp/"
f1 = request.urlopen(f1)
f1 = f1.read()
f1 = f1.decode('utf-8')
soup = BeautifulSoup(f1, 'html.parser')
es = soup.find_all("img")
shuchu = str(es)
print(shuchu)
kz = 0
f2 = ""
ii = 0
for i in range(len(shuchu)):
    c = shuchu[i:i+4]
    if c == "http":
        kz = 1
    if c == ".jpg":
        kz = 2
    if kz == 1:
        f2 = f2 + shuchu[i]
    if kz == 2:
        if ii == 46or ii == 126:
            ii = ii + 1
            f2 = ""
            kz = 0
            continue
        f2 = f2 + shuchu[i]+shuchu[i+1] + shuchu[i+2] + shuchu[i+3]
        if ii % 2 == 0:
            request.urlretrieve(f2, r"C:Users\李佳欣\Desktop\py\pa\%d.jpg" % (ii//2))
            print(f2, "已完成，保存为%d.jpg" % (ii//2))
        ii = ii+1
        f2 = ""
        kz = 0