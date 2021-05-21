nums = [1,1,2,3]


## little optimized  

i = 0
res = []
while i<len(nums):
    res+=([nums[i+1]]*nums[i])
    i+=2
print(res)



# temp=[]
# for f in range(0,len(nums),2):
#     k = nums[f]
#     while k!=0:
#         temp.append(nums[f+1])
#         k-=1
# print(temp)