def getMoneySpent(keyboards, drives, b):
    
    if len(keyboards) == 1 and keyboards[0] >= b:
        return -1
    if len(drives) == 1 and drives[0] >= b:
        return -1
    n = []
    for x in keyboards:
        for y in drives:
            temp = x+y
            if temp>b:
                continue
            else:
                n.append(temp)
    if not n:
        return -1
    return max(n)                  