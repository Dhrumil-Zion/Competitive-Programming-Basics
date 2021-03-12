def insertionSort2(n, a):
    for i in range(1,n):
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
        print(*a)

arr = [1, 4, 3, 5, 6, 2]
n=len(arr)
insertionSort2(n,arr)












# arr =[2 ,4 ,6 ,8 ,3]
 
# target = arr[-1]
# idx = len(arr)-2

# while (target < arr[idx]) and (idx >= 0):
#     arr[idx+1] = arr[idx]
#     print(*arr)
#     idx -= 1

# arr[idx+1] = target
# print(*arr)