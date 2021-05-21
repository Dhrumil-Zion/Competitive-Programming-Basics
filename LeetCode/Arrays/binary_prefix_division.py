nums = [1,1,1,0,1]

answer = []
l = len(nums)
num = 0
for i in range(l):
    if nums[i]==0 and not num:
        answer.append(True)
    else:
        num = ((num*2)+(nums[i]==1))%5
        if not num:
            answer.append(True)
        else:
            answer.append(False)
print(answer)



# result_list=[]
# for i in range(len(nums) + 1):
#     for j in range(i + 1, len(nums) + 1):
#         result_list.append(nums[i:j])
#     if len(nums[i:j])==len(nums):
#         break
# temp=[]
# for r in result_list:
#     if int("".join(map(str, r)))%5==0:
#         temp.append(True)
#     else:
#         temp.append(False)
# print(temp)