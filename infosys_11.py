T= int(input())
sum_sam = 0        
sum_bob = 0
rods =[]
while T!=0:
    rods.append(int(input()))
    T-=1
g = -1
while len(rods)!=0:
    g+=1
    rods.sort()
    c = rods[-1]
    rods.remove(c)
    if g%2==0:
        sum_sam+=c
    else:
        sum_bob+=c
    if c>1:
        rods.append(int(c/2))
print(sum_sam)