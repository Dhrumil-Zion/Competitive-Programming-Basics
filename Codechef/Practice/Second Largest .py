T=int(input())
while T!=0:
    nums = list(map(int,input().split()))
    nums.sort()
    print(nums[-2])
    T-=1