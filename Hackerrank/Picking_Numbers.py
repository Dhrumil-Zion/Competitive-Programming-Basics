def pickingNumbers(a):
    temp = []
    arr = []
    a.sort()
    for x in range(len(a)):
        arr.clear()
        arr.append(a[x])
        for y in range(x+1,len(a)):
            if abs(a[y]-a[x]) <=1:
                arr.append(a[y])
        temp.append(len(arr))
    return max(temp)