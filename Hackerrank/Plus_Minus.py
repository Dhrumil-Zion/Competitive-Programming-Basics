def plusMinus(arr):
    n,z,p =0,0,0
    l =len(arr)
    c = 0
    a = []
    for x in arr:
        if x < 0:
            n +=1
        elif x == 0:
            z +=1
        elif x > 0:
            p +=1    
    a.append(p)
    a.append(n)
    a.append(z)            
    while c!=3:        
        print("{:.6f}".format(a[c]/l))
        c +=1