arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
arr = [1,1,2,2,3]
a = 0
b = 0 
c = 1
count=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                count+=1
print(count)