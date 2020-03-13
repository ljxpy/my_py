for i in range(100, 1000):
    z = i**2
    if z < 100000:#99 999
        z = z % 1000
        if z == i:
            print(z)
    if z > 100000:
        z = z % 1000
        if z == i:
            print(z)