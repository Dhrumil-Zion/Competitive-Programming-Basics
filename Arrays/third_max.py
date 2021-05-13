nums= [2,2,3,1]

temp = list(set(nums))
if len(temp)<3:
    print(max(list(set(nums))))
else:
    temp.sort()
    print(temp[-3])
