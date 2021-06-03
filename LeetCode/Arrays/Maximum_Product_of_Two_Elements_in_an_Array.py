class Solution:
    def maxProduct(nums):
        x = max(nums)   
        nums.remove(x)
        y = max(nums)    
        return (x-1)*(y-1)

# time complexity is n^2 which is much high but leetcode accepted solution 

# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         arr = []
#         for c in range(len(nums)):
#             for d in range(c+1,len(nums)):
#                 arr.append((nums[c]-1)*(nums[d]-1))
#         return max(arr)
        