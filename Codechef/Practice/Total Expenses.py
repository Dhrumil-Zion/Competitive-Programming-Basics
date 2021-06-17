t=int(input())
while t!=0:
    q,p = map(int,input().split())
    total = q*p
    if q<1000:
        print("{:.6f}".format(total))
    elif q>1000:
        print("{:.6f}".format(total - (total*0.1)))
    t-=1