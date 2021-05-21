nums = [1,3,5,6]
target = 2
if target not in nums:
    nums.append(target)
    nums.sort()
print(nums.index(target))