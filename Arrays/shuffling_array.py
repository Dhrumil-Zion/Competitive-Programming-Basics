nums = [2,5,1,3,4,7]
n = 3
final=[]
temp = nums[:n]
temp2= nums[n:]
for g in range(n):
    final.append(temp[g])
    final.append(temp2[g])
print(final)
