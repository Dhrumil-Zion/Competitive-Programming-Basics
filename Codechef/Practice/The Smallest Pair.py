t =int(input())
while t!=0:
    n =int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[0]+arr[1])
    t-=1