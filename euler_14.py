def collatz(n):
    niz=[]
    while n != 1:
        if n % 2 == 0:
            n /= 2
            niz.append(n)
        else: 
            n = 3*n+1
            niz.append(n)
    return len(niz)

max = 0
for i in range (2,1000000):
    temp = collatz(i)
    if temp > max:
        max = temp    
        
print max
