# 2
# 1 4
# 2 3
T =int(input())
while T!=0:
    times,n = map(int,input().split())
    for _ in range(times):
        n=(n*(n+1)/2)
    print(int(n))
    T-=1