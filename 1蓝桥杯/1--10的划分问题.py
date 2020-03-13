#1--10的划分问题
n = int(input("输入："))
su = 0
def d(n):
    global su
    for a in range(n):
        for b in range(n):
            if n == a+b:
                print(a, "+", b)
                su = su + 1
d(n)
if su % 2 == 0:
    print("有", su/2, "次")
elif su % 2 == 1:
    print("有", (su+1)/2, "次")