# sourcery skip: hoist-statement-from-if, remove-pass-body

return_arr =[]
temp=[]
target =[1,2]
n=4
# [1,2,3]
# 3
# [1,2]
# 4
# [2,3,4]
# 4

arr = [c for c in range(1,n+1)]
for v in arr:
    if temp==target:
        break
    if v in target:
        return_arr.append("Push")
        temp.append(v)
    else:
        return_arr.append("Push")
        return_arr.append("Pop")
print(return_arr)