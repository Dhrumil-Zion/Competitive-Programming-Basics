def diagonalDifference(arr):
    su1 = 0
    su2 = 0
    count2 = len(arr) - 1
    for count1, x in enumerate(arr):
        su1 += x[count1]
        su2 += x[count2]
        count2 -=1
    if su1 > su2:
        return (su1 - su2)
    else:
        return (su2 - su1)