import math
def majorityElement(nums):
    return [v for v in set(nums) if nums.count(v)>math.floor(len(nums)/3)]