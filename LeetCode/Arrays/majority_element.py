import math
def majorityElement(nums):
    for c in set(nums):
        if nums.count(c)> math.floor(len(nums)/2):
            return c
print(majorityElement([1,2,2,2,1,1,1,1,1,1,2,1]))