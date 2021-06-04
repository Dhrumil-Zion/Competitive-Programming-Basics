import itertools
from functools import reduce

N,M = map(int,input().split())
x = [c for c in range((2**M))]
print(x)
c = 0 
for each in itertools.permutations(x,N):
    res = reduce(lambda x, y: x & y, each)
    if res==0:
        print(each)
        c+=1
print(c)