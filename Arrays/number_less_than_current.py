nums=[7,7,7,7]
temp = []
k=0
for c in nums:
    for f in nums:
        if c>f:
            k+=1
    temp.append(k)
    k=0
print(temp)