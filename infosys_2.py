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


import math
from itertools import combinations


# def solution(A):
#     m = math.floor(0)
#     i = len(A)
#     while i >= 0:
#         subarrayslist = set(combinations(A, i))
#         for array in subarrayslist:
#             if array:
#                 S = sum(array)
#                 R = array[0]
#                 for a in range(1, len(array)):
#                     R = R | array[a]
#                 beauty = math.floor((S / R)*10000)
#                 if m < beauty:
#                     m = beauty
#         i -= 1
#     print(m)


# A = []
# for _ in range(int(input())):
#     A.append(int(input()))
# solution(A)