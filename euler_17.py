dict = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 100: 7, 1000: 8}

def less_than(n):
    sum = 0
    if n in dict: 
        sum += dict[n] 
    else:
        sum = dict[int(str(n)[1:2])] + dict[n // 10 * 10]
    return sum

s = 0

for i in range (1,1001):
    if i < 100: 
        s += less_than(i)
    else:
        a = dict[i // 100] + dict[100] + 3
        b = (i - i//100*100 )
        s += a + less_than(b)
