month = {"jan": 3, "feb": 1, "mar": 3, "apr": 2, "may": 3, "jun": 2, "jul": 3, "avg":3, "sept": 2, "okt": 3, "nov": 2, "dec": 3}
leapmonth = {"jan": 3, "feb": 0, "mar": 3, "apr": 2, "may": 3, "jun": 2, "jul": 3, "avg":3, "sept": 2, "okt": 3, "nov": 2, "dec": 3}
mapmonth = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, "jul": 7, "avg":8, "sept": 9, "okt": 10, "nov": 11, "dec": 12}
dan = {"pon": 1, "uto": 2, "sre": 3, "cet": 4, "pet": 5, "sub": 6, "ned": 0}

god = 1901
dan = 1
count = 0
while god < 2001:
    if god % 4 == 0 :
        for m in sorted(leapmonth, key=mapmonth.__getitem__):
            dan += int(month[m])
            dan %= 7
            if dan % 7 == 0: count += 1
    else:
        for m in sorted(month, key=mapmonth.__getitem__):
            dan += int(month[m])
            dan %= 7
            if dan % 7 == 0: count += 1
        
    god += 1
