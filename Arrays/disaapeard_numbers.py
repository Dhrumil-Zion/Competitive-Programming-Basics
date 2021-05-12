nums = [4,3,2,7,8,2,3,1]

s=set(nums)
temp = [i for i in range(1,len(nums)+1) if i not in s]
print(temp)


# v = [c for c in range(1,len(nums)+1)]
# temp = []
# for g in v:
#     if g in nums:
#         continue
#     else:
#         temp.append(g)
# print(temp)