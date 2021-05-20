def luckBalance(k, contests):
    a = []
    b = []
    for x in contests:
        if x[1] == 1:
            a.append(x[0])
        else:
            b.append(x[0])
    a.sort()
    if k > len(a):
        return sum(a)+sum(b)
    return sum(a[len(a)-k:]) + sum(b) - sum(a[:len(a)-k])