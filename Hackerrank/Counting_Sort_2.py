def countingSort(arr):
    a = []
    c = []
    for x in range(100):
        z =arr.count(x)
        for _ in range(z):
            c.append(x)
    c.sort()
    return c