def getTotalX(a, b):
    
    pre = []
    prepre = []
    lis = [x for x in range(a[-1],b[0]+1)]
    for x in lis:
        c=0
        for y in a:
            if x%y==0:
                c+=1
        if c == len(a):
            s=0
    for x in pre:
        c=0
        for y in b:
            if y%x==0:
                c+=1
        if c==len(b):
            s+=1        
           
    print(s)        



    

a = [2,4]
b = [16,32,96]
getTotalX(a,b)    