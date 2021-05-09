from functools import reduce
from operator import ior
from itertools import combinations
import math
T= int(input())
arr =[]
temp =[]
temp2 = []
while T!=0:
    arr.append(int(input()))
    T-=1
for r in range(2,len(arr)+1):
    temp2 +=list(combinations(arr, r))
for c in temp2:
    res = reduce(ior, c)
    temp.append(sum(c)/res)
print(math.floor(max(temp)*10000))
