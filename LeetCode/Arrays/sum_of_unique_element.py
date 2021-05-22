class Solution:
    def sumOfUnique(nums):
        return sum(f for f in set(nums) if nums.count(f)<=1)