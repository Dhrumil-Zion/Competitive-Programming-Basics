import itertools

l=[4] 

j = list(set(list(itertools.combinations(l, 1))))
c=0
for x in j:
    if sum(x) == 4:
        c+=1  

print(c)        