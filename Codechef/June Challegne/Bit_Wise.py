MOD=1000000007
T = int(input())
while (T!=0):
    x= 2
    res =1
    ans=1
    n,m = map(int,input().split())
    while (n > 0):
        if (n & 1):
            ans = (ans*x) % MOD
        n = n>>1
        x = x**2 % MOD
    ans -= 1
    while (m > 0):
        if (m & 1):
            res = (res*ans) % MOD
        m = m>>1
        ans = ans**2 % MOD
    print(res)
    T-=1
















# import itertools
# from functools import reduce

# N,M = map(int,input().split())
# x = [c for c in range((2**M))]
# print(x)
# c = 0 
# for each in itertools.permutations(x,N):
#     res = reduce(lambda x, y: x & y, each)
#     if res==0:
#         print(each)
#         c+=1
# print(c)