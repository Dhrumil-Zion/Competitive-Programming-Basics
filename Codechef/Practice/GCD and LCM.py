import math
t=int(input())
while t!=0:
    t-=1
    n1,n2 =map(int,input().split())
    gcd = math.gcd(n1,n2)
    lcm = (n1*n2)//gcd
    print("{} {}".format(gcd,lcm))