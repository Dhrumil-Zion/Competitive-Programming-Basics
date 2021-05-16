def divisibleSumPairs(n, k, ar):
    temp = []
    for c in range(len(ar)):
        for g in range(c,len(ar)):
            if c < g and (ar[c]+ar[g]) % k == 0:
                temp.append([ar[c],ar[g]])
    return len(temp)