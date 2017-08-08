M=[]
with open('triangle') as f:
    for line in f:
        M.append([int(i) for i in line.rstrip('\n').split(" ")])
        
for m in range(len(M)-2,-1,-1):
    for n in range(len(M[m])):
        M[m][n] = max(M[m+1][n],M[m+1][n+1]) + M[m][n]
print M[0][0]
