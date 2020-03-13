x = 'https://hong.tianzhen-zuida.com/20200209/19971_59b58144/1000k/hls/911e0ded0d3'
from urllib import request
for i in range(1455,1456):
    if i > 99999:
        i = str(i)
    elif i > 9999:
        i = str(i)
        i = "0" + i
    elif i > 999:
        i = str(i)
        i = "00" + i
    elif i > 99:
        i = str(i)
        i = "000" + i
    elif i>9:
        i = str(i)
        i = "0000" + i
    else:
        i = str(i)
        i = "00000" + i
    i = i + ".ts"
    url = x + i
    print(url)
    request.urlretrieve(url,  r"C:Users\李佳欣\Desktop\py\pa\mov\叶问4\%s" % i)
    print(i, "已完成")
