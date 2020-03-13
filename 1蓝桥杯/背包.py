#背包2
n, m = input().split()
n = int(n)
m = int(m)

w = [0]
v = [0]
for i in range(n-1):
    w = w+[0]
    v = v+[0]
for i in range(n):
    w1, v1 = input().split()
    w1 = int(w1)
    v1 = int(v1)
    w[i] = w[i]+(w1-0.000001)
    v[i] = v[i]+(v1)

d = {}
for i in range(n):
    d.update({v[i]/w[i]:[v[i],w[i]]})
sorted(d.keys())
vv = 0
for key in d:
    if d[key][1] <= m:
        vv = d[key][0]+vv
        m = m-d[key][1]
print(vv)