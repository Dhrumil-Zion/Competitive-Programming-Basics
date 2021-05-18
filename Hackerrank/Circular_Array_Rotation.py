def circularArrayRotation(a, k, queries):
    # le = len(a)
    # ro = 1
    for _ in range(1,k+1):
        s = a.pop()
        a.insert(0,s)
    return [a[x] for x in queries]    