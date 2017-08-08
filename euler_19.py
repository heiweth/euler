month = {"jan": 3, "mar": 3, "apr": 2, "may": 3, "jun": 2, "jul": 3, "avg":3, "sept": 2, "okt": 3, "nov": 2, "dec": 3}
dan = {"pon": 1, "uto": 2, "sre": 3, "cet": 4, "pet": 5, "sub": 6, "ned": 0}
god = 1901
dan = 1
count = 0
while god < 2001:
    for m in month:
       dan += int(month[m])
       dan %= 7
       if dan % 7 == 0: count += 1
    if god % 4 == 0 : dan += 1
    god += 1
