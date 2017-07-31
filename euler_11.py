z=1
m=1
i=3
a=sum(range(i))
while True :
    for j in range (1,a/2+1):
        if a % j == 0 :
            z += 1
    m = z
    if m >= 200 : break 
    z=1
    i += 1
    a=sum(range(i))
  
print a
