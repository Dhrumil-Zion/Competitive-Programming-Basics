T = int(input())
answer = []
while T > 0:
    length = int(input())
    li2 = [int(x) for x in input().split()]
    ar = [x for x in range(1,length+1)]
    answer.append(list(list(set(ar)-set(li2)) + list(set(li2)-set(ar))))        
    T = T - 1    
for x in answer:
    for y in x:
        print(y)    
