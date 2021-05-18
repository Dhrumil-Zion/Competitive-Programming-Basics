def cutTheSticks(arr):
    ans = [len(arr)]
    while 1:
        z = min(arr)
        for x in range(len(arr)):
            arr[x] = arr[x]-z
        arr = list(filter(lambda x: x != 0, arr))
        if not arr:
            break
        ans.append(len(arr))
    return ans