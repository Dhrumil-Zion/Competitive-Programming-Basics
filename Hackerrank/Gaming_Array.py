def gamingArray(arr):
    count=0 
    m=0 
    for i in arr:
        if i>m:
            m=i
            count+=1
    if count%2==0:
        return 'ANDY'
    return 'BOB'