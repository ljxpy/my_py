#ab和cd三次方相等
for a in range(1, 30):
    for b in range(1, 30):
        for c in range(1, 30):
            for d in range(1, 30):
                if a**3+b**3 == c**3+d**3 and a != b != c != d and a != c and b != d and a != d:
                    x1 = max(a, b, c, d)
                    x4 = min(a, b, c, d)
                    x2 = max({a, b, c, d}-{x1, x4})
                    x3 = max({a, b, c, d}-{x1, x2, x4})
                    print(x1, ",", x2, ",", x3, ",", x4)