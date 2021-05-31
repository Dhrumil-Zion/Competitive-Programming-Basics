arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2
count =0
t=0
for c in arr1:
    for k in arr2:
        if abs(c-k) <= d:
            break
        else:
            count+=1
    if count==len(arr2):
        t+=1
    count=0
print(t)