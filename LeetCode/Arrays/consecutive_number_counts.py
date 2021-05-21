a = [1,1,0,1,0,1,1,1]

#### Optimized one 

c=m=0
for i in a:
    if i==0:
        m=max(m,c)
        c=0               
        continue
    c+=1
print(max(m,c))

# count = 0
# temp = []
# for c in a:
#     if c==1:
#         count+=1
#         continue
#     else:
#         temp.append(count)
#         count=0
# temp.append(count)
# print(max(temp))