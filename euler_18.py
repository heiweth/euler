a = []
a.append("75")
a.append("95 64")
a.append("17 47 82")
a.append("18 35 87 10")
a.append("20 04 82 47 65")
a.append("19 01 23 75 03 34")
a.append("88 02 77 73 07 63 67")
a.append("99 65 04 28 06 16 70 92")
a.append("41 41 26 56 83 40 80 70 33")
a.append("41 48 72 33 47 32 37 16 94 29")
a.append("53 71 44 65 25 43 91 52 97 51 14")
a.append("70 11 33 28 77 73 17 78 39 68 17 57")
a.append("91 71 52 38 17 14 91 43 58 50 27 29 48")
a.append("63 66 04 68 89 53 67 30 73 16 69 87 40 31")
a.append("04 62 98 27 23 09 70 98 73 93 38 53 60 04 23")

M = [i.split() for i in a]
M = [[int(j) for j in i] for i in M]


sum = 0
maximum = 0
p = 15
m = 14

def max(a,b):
    if a >= b: return a
    else: return b

for m in range(14,-1,-1):
    C=[0]*len(M[m-1])
    for n in range(1,len(M[m])):
        if M[m][n] > M[m][n-1]:
            if n > len(M[m-1])-1: 
                C[n-1] = M[m][n] + M[m-1][n-1]
            else: 
                C[n-1] = M[m][n] + max(M[m-1][n],M[m-1][n-1])
        else: 
            if n > len(M[m-1])-1: C[n-1] = M[m][n-1] + M[m-1][n-1]
            else: C[n-1] = M[m][n-1] + max(M[m-1][n-1],M[m-1][n-2])
    M[m-1] = C
    sum = M[m-1][0]
    del M[m]        

        
