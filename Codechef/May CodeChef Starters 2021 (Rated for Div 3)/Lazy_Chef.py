T = int(input())
while T!=0:
    x,m,d =map(int,input().split())
    print(min(x*m,x+d))
    T-=1