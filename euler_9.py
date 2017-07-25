from math import sqrt
for a in range(1,500):
    for b in range(1,500):
        c = a*a + b*b
        if a+b+sqrt(c) == 1000:
            print a,b,sqrt(c)
            break
