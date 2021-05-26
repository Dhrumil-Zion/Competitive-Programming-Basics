import math

## Optimized one

def isPowerOfThree(n):
    if n == 0:
        return False
    while n % 3 == 0:
        n /= 3
    return n == 1

## Brute-Force Method

def isPowerOfThree(n):
    return any(math.pow(3,c)==n for c in range(21))

print(isPowerOfThree(21323))