def isPowerOfTwo(n):
    if n == 0:
        return False
    while n % 2 == 0:
        n /= 2
    return n == 1
print(isPowerOfTwo(2176))