def pageCount1(n,p):                #### Most optimized code  ####
    return min(p//2, n//2 - p//2)
def pageCount(n, p):
    temp = []
    clef = 0
    crig = 0
    temp.append([1])
    for x in range(2,n+1,2):
        temp.append([x,x+1])
    if n%2==0:
        temp.append([n])                     
    for x in temp:
        if p in x:
            break
        else:
            clef+=1
    temp.reverse()
    
    if n %2==0:
        temp.pop(0)
    for x in temp:
        if p in x:
            break
        else:
            crig+=1                  
    return min(clef,crig)

ans = pageCount(5,4)
de = pageCount1(5,4)
print(ans)
print(de)

