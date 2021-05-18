def findDigits(n):
    t=n
    c=0
    while n!=0:
        temp = n%10
        n=int(n/10)
        if temp ==0:
            continue
        if t%temp==0:
            c+=1
    return c