from collections import defaultdict
def equalizeArray(arr):
    l = []
    n=len(arr)
    d = defaultdict(lambda: 0)
    for i in range(n):
        d[arr[i]] += 1
    arr.sort(key=lambda x: (-d[x], x))
    t = arr[0]
    arr.remove(t)
    res = [i for i in arr if i != t] 
    return len(res)