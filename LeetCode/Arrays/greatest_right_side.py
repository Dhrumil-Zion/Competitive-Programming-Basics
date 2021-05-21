arr = [17,18,5,4,6,1]
for c in range(len(arr)-1):
    arr[c] = max(arr[c+1:])
arr[-1]=-1
print(arr)
