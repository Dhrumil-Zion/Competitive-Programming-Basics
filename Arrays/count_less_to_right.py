from bisect import bisect_left
nums = [5,2,6,1] 

res = [0] * len(nums)
s_nums = sorted(nums)
for idx,n in enumerate(nums):
    j = bisect_left(s_nums, n) 
    res[idx] = j              
    s_nums.pop(j)            
print(res)



# temp2 = []
# k=0
# for c in range(len(nums)-1):
#     temp = nums[c+1:]
#     for f in temp:
#         if nums[c]>f:
#             k+=1
#     temp2.append(k)
#     k=0
# temp2.append(0)
# print(temp2)
