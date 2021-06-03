class Solution:
    def minOperations(self, nums: List[int]) -> int:
        pre,ans=0,0
        for i in nums:
            if pre < i:
                pre=i
            else:
                pre+=1
                ans+=pre-i
        return ans