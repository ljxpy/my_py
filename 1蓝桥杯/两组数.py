import random
zuix = []
def jisuan(n, x1, x2):
    ccc = 0
    for i in range(n):
        ccc = x1[i]*x2[i] + ccc
    return ccc
def yizu():
    n = int(input())
    xx1 = input().split(" ")
    x1 = []
    for c in range(len(xx1)):
        x1.append(int(xx1[c])) #由字符串变成int形式
    xx2 = input().split(" ")
    x2 = []
    for c in range(len(xx2)):
        x2.append(int(xx2[c]))
    daxiao = []
    for qqq in range(1000):
        suiji = []
        for i in range(n):
            suiji.append(random.random())
        x3 = dict(zip(suiji, x1))
                #paixu
        x3pai = dict(sorted(x3.items()))
        x4 = list(x3pai.values())
        daxiao.append(jisuan(n, x4, x2))
    zuix.append(min(daxiao))
nn = int(input())
for i in range(nn):
    yizu()
for i in range(nn):
    print(zuix[i])