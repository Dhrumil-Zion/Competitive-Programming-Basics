def subsets(nums):
    def dfs(nums, target, path, res):
        if target > 0:
            target -= 1
        elif target == 0:
            res.append(path)
        for i in range(len(nums)):
            dfs(nums[i+1:], target, path + [nums[i]], res)
    res = [[]]
    dfs(nums, 1, [], res)
    return res

from itertools import combinations
def subsets(nums):
    subs = []
    for i in range(len(nums)+1):
        temp = [list(x) for x in combinations(nums, i)]
        if temp:
            subs.extend(temp)
    return subs
print(subsets([1,2,3,]))