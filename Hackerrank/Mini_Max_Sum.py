def miniMaxSum(arr):
    su1 = 0
    su2 = 0
    c = 0
    n = -1
    arr.sort()
    while (c!=4):
        su1 += arr[c]
        su2 += arr[n]
        c +=1
        n -=1
    print("{} {}".format(su1,su2)) 