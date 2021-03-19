import math
def squares(a, b):
    c  = int(math.sqrt(a))
    d = int(math.sqrt(b))
    print(c)
    print(d)
    su = d-c
    if c**2 == a:
        su +=1
    if d**2 == b:
        su+=1
    print(su)    
    # c= 0 
    # lis = [x for x in range(a,b+1)]
    # z = [x for x in range(int(math.sqrt(a)),int(math.sqrt(b)+1))]
    # for x in z:
    #     if x**2 in lis:
    #         c+=1
    # print(c) 

squares(3,9)    
#squares(465868129,988379794)    
