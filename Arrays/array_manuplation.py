arr = [0,4,1,0,0,8,0,0,3]
ini_l = len(arr)
c= 0
count  = 0
k = len(arr)+arr.count(0)
try:
    while k!=0:
        if arr[c]==0:
            arr.insert(c,0)
            c+=1
        c+=1
        k-=1
except:
    for _ in range(len(arr)-ini_l):
        arr.pop()
print(arr)
