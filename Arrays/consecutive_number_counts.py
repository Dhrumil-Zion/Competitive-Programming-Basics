a = [1,1,0,1,0,1,1,1]

count = 0
temp = []
for c in a:
    if c==1:
        count+=1
        continue
    else:
        temp.append(count)
        count=0
temp.append(count)
print(max(temp))