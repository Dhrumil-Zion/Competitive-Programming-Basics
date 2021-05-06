## https://www.hackerrank.com/challenges/maximum-perimeter-triangle/

import itertools
from itertools import combinations, chain

def maximumPerimeterTriangle(sticks):
    pairs = set(combinations(sticks, 3))
    selectedpair = None
    max = 0
    for pair in pairs:
        if (
            pair[0] + pair[1] > pair[2]
            and pair[0] + pair[2] > pair[1]
            and pair[1] + pair[2] > pair[0]
            and max < sum(pair)
        ):
            max = sum(pair)
            selectedpair = pair
    if selectedpair:
        selectedpair = list(selectedpair)
        selectedpair.sort()
        return selectedpair
    return [-1]

print(maximumPerimeterTriangle([1,2,3,4,5,10]))
# # def findsubsets(s, n):
# #     return list(map(list, itertools.combinations(s, n)))

# # s =[1 ,1 ,1 ,3 ,3]
# # # s = [1,2,3,4,5,10]
# # n = 3
# # new_arr = findsubsets(s, n)
# # temp = []
# # new_temp=[]
# # ma_pre = 0
# # final =[]

# # for c in new_arr:
# #     if c[0]+c[1]>c[2] and c[1]+c[2]>c[0] and c[0]+c[2]>c[1]:
# #         if sum(c)>ma_pre:
# #             ma_pre =sum(c)
# #         temp.append(c)

# # if len(temp)>1:
# #     for t in temp:
# #         if sum(t) == ma_pre:
# #             new_temp.append(t)

# #     if len(new_temp)>1:
# #         ma_side = max(max(new_temp))
# #         for y in new_temp:
# #             if max(max(y)) == ma_side:
# #                 final.append(y)
# #         if len(final)>1:
# #             print(final[0])
# #         else:
# #             print(final[0])
# #     else:
# #         print(new_temp[0])
# # else:
# #     print(-1)


# # import itertools
# # from itertools import combinations, chain

# # def findsubsets(s, n):
# #     return list(map(list, itertools.combinations(s, n)))

# # def maximumPerimeterTriangle(sticks):
# #     s = sticks
# #     n = 3
# #     new_arr = findsubsets(s, n)
# #     temp = [
# #         c
# #         for c in new_arr
# #         if c[0] + c[1] > c[2] and c[1] + c[2] > c[0] and c[0] + c[2] > c[1]
# #     ]

# #     if temp:
# #         return max(temp)
# #     else:
# #         return list([-1])

# # print(maximumPerimeterTriangle([1,2,3,4,5,10]))

# import itertools
# from itertools import combinations, chain

# def findsubsets(s, n):
#     return list(map(list, itertools.combinations(s, n)))

# def maximumPerimeterTriangle(sticks):
#     s = sticks
#     n = 3
#     new_arr = findsubsets(s, n)
#     temp = []
#     max_peri = []
#     for c in new_arr:
#         if c[0]+c[1]>c[2] and c[1]+c[2]>c[0] and c[0]+c[2]>c[1]:
#             temp.append(c)
#     if len(temp)>0:
#         for e in temp:
#             max_peri.append(sum(e))
#         return temp[max_peri.index(max(max_peri))]
#     else:
#         return list([-1])
# print(maximumPerimeterTriangle([1,2,3,4,5,10]))