def beautifulDays(i, j, k):
    days = [x for x in range(i,j+1)]
    c=0 
    for n in days:
        rev = 0
        t=n
        while(n > 0):
            a = n % 10
            rev = rev * 10 + a
            n = n // 10    
        if  abs(t-rev)%k ==0:
            c +=1
    return c