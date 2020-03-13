#回文数
def huan(y, mu, n):
    c = n[y]
    n[y] = n[y+1]
    n[y+1] = c
    if y+1 != mu:
        huan(y+1, mu, n)
n = list(input("输入字符串"))
s = {}
for i in n:
    sum = 0
    for ii in n:
        if i == ii:
            sum = sum+1
            s[i] = sum
sum = 0
dan = '@'
for i in s:
    if s[i] % 2 == 1:
        sum = sum + 1
        dan = i
        n = list(n)
        n.remove(i)
if sum > 1:
    print("不能组成回文数")
    exit()
#排序
l = len(n)//2
for i in range(l):
    c = 0
    for ii in range(i, len(n)-1-i):
        if n[i] == n[ii]:
            c = c+1
        if n[i] == n[ii] and c == 2:
            huan(ii, len(n)-1-i, n)
            break
if dan != '@':
    n = list(n)
    n1 = n[:len(n)//2]
    n2 = n[len(n)//2:]
    n1.append(dan)
    n = n1 + n2
print("重新排序得到的回文数：", end='')
for i in n:
    print(i, end='')