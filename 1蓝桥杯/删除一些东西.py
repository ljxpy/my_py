x = input()
y = input()
chang = len(x)
xx = ""
for c in range(chang):
    if y is x[c]:
        continue
    xx = xx+(x[c])
print(xx)