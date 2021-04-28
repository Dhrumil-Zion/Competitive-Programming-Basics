T = int(input())
while T:
    n,x = [int(g) for g in input().split()]
    arr = [int(g) for g in input().split()]
    g = sum(arr[c] > x for c in range(n))
    print(g)
    T-=1
    