a = [1 ,2 ,3,3]
for x in range(len(a)):
    if x ==0 and sum(a[1:])==0:
        print("YES")
    s1 = a[:x]
    s2 = a[x+1:]
    if sum(s1) == sum(s2):
        print("YES")            
