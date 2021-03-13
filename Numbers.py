def cutTheSticks(arr):
    ans = []
    ans.append(len(arr))
    while 1:
        z = min(arr)
        for x in range(len(arr)):
            arr[x] = arr[x]-z
        arr = list(filter(lambda x: x != 0, arr))     
        if len(arr) == 0:
            break    
        ans.append(len(arr))    
    print(ans)

arr = [1 ,2 ,3 ,4, 3, 3, 2, 1]
cutTheSticks(arr)