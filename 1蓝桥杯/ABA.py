''' A1 =        “A”
　　A2 =       “ABA”
　　A3 =     “ABACABA”
　　A4 = “ABACABADABACABA”'''

s ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sum = ''
n = input("亲输入大写字母：\n")
nn = ord(n)-64
for i in range(0, nn):
    sum = sum+s[i]+sum
print(sum)