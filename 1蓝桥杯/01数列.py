for i in range(0, 11112):
    a0 = i/10000
    a1 = int(i / 1000 % 10)
    a2 = int(i/100 % 10)
    a3 = i/10 % 10
    a4 = i % 10
    if a1 < 2 and a2 < 2 and a3 < 2 and a4 < 2:
        if i >= 10000:
           print(i)
        elif i >= 1000:
             print("0%d" %i)
        elif i >= 100:
             print("00%d" %i)
        elif i >= 10 :
             print("000%d" %i)
        elif i >= 0 :
             print("0000%d"%i)
