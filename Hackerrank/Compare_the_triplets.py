def compareTriplets(a, b):
    pa = 0
    pb = 0
    l = len(a)
    c =[]
    for x in range(l):
        if a[x] > b[x]:
            pa +=1
        elif a[x] < b[x]:
            pb +=1
        elif a[x] == b[x]:
            continue
    c.append(pa)
    c.append(pb)
    return c   