def minimumDistances(a):
    f = []
    for x in range(len(a)):
        if a.count(a[x])>1:
            index_pos_list = [ i for i in range(len(a)) if a[i] == a[x] ]
            f.append(abs(index_pos_list[0]-index_pos_list[1]))
    if f:
        f.sort()
        return f[0]
    else:
        return -1