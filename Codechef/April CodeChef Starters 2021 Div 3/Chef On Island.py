# Problem Code: CCISLAND

T=int(input())
while T!=0:
    X,Y,x,y,D = map(int,input().split())
    if D*x <=X and D*y<=Y:
        print("YES")
    else:
        print("NO")
    T-=1