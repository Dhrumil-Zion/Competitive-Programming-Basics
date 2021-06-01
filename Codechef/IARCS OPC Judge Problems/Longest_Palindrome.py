def subString(s, n):
    palindrom=[]
    size =[]
    for i in range(n):
        for li in range(i+1,n+1):
            st = s[i: li]
            if st==st[::-1]:
                palindrom.append(st)
                size.append(len(st))
    print(max(size))
    print(palindrom[size.index(max(size))])

    
s = "amma"
subString(s,len(s))
