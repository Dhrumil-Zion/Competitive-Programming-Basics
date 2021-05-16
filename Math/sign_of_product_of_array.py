nums = [-1,-2,-3,-4,3,2,1]
if 0 in nums:
    print(0)
elif sum(c<0 for c in nums)%2==0:
    print(1)
else:
    print(-1)