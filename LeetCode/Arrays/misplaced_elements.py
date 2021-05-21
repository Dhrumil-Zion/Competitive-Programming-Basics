a = [1,1,4,2,1,3]
b =a.copy()
a.sort()
k=0
c=0
while k != len(b):
    if a[k]==b[k]:
        k+=1
        continue    
    else:
        c+=1
        k+=1

print(c)