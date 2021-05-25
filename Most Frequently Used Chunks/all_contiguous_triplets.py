a = [10,2,1,4,5,6,7]
le = len(a)
temp = []
for i in range(le-2):
    t = a[i:i+3]
    if t[0]>t[1] and t[1]>t[2]:
        temp.append(a[i:i+3])
print(temp)
