from itertools import accumulate
def runningSum(nums):
    print(list(accumulate(nums)))

# def runningSum(nums):
#     temp = []
#     su = 0
#     for c in nums:
#         su+=c
#         temp.append(su)
#     print(temp)

runningSum([1,2,3,4,5])
