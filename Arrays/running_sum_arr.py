a = [1,2,3,4,5,6]
temp =[]
summ =0
for k, f in enumerate(a):
    summ+=f
    a[k]=summ
print(a)

# j = 1
# for i in range(len(nums)-1):
#     nums[j] = nums[i] + nums[j]   
#     j +=1
# return nums