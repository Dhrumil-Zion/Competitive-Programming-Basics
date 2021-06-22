t= int(input())
while t!=0:
    n,m=map(int,input().split())
    flag =0
    for _ in range(n):
        st =input()
        for d in st:
            flag^=(int(d)-0)
    if flag!=0:
        print("YES")
    else:
        print("NO")
    t-=1