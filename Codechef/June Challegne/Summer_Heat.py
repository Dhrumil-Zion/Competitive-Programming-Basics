T = int(input())
while T!=0:
    xa,xb,Xa,Xb = map(int,input().split())
    print((Xa//xa)+(Xb//xb))
    T-=1