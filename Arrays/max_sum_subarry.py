nums = [5,4,-1,7,8]
# print(max(sum(nums[i:i+j]) for i in range(len(nums)) for j in range(1,len(nums)-i+1)))
n=len(nums)
if n==1:
    print(nums[0])
dp=[0]*n
dp[0]=nums[0]
maxnum=nums[0]
for i in range(1,n):
    dp[i]=max(nums[i],nums[i]+dp[i-1])
    maxnum=max(maxnum,dp[i])
    print(dp)
    print(maxnum)
print(maxnum)