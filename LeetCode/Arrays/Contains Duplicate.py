def containsDuplicate(nums):
    return len(nums)!=len(list(set(nums)))

print(containsDuplicate([1,2,3,1]))