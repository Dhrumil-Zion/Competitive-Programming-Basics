def figOutnum(n):
    fibo = []
    n1,n2 = 0, 1
    if n <= 0:
        fibo.append(0)
    elif n == 1:
        fibo.append(1)
    else:
        fibo.append(1)
        for _ in range(n):
            nth = n1 + n2
            fibo.append(nth)
            n1 = n2
            n2 = nth
    if n in fibo:
        print(n)
    else:
        sum = sum(v for v in fibo if v<n and v%2!=0)
        print(sum)
        
figOutnum(20)