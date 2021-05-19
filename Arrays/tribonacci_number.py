def tribonacci(n):
    a = 0
    b = 1
    c = 1
    if n == 0:
        return 0
    elif n in [1, 2]:
        return 1
    else:
        temp = [0,1,1]
        for _ in range(2, n):
            d = a + b + c 
            temp.append(d)
            a = b
            b = c
            c = d
        return temp[-1]

print(tribonacci(25))
