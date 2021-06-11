def containsNearbyDuplicate(nums, target,t):
    d = {}
    for k,v in enumerate(nums):
        if v in d and k - d[v] <= target and (nums[k] - nums[v])<t:
            return True
        d[v] = k
    return False
nums = [1,0,1,1] 
k = 1
t = 2
nums = [1,5,9,1,5,9]
k = 2
t = 3
print(containsNearbyDuplicate(nums,k,t))