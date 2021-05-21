
## Optimized one

from math import sqrt
def fib(n):
    sqrt5 = sqrt(5)
    return int((pow(1 + sqrt5, n) - pow(1 - sqrt5, n)) / pow(2, n) / sqrt5)
print(fib(9))

## Slower than above one 
def fibo_things(n):
    a = 0
    b = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        temp = [0,1]
        for _ in range(2, n):
            c = a + b
            temp.append(c)
            a = b
            b = c
        return sum(temp)

n=4
sum = fibo_things(n-1) + fibo_things(n-2)
print(sum)
