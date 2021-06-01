def primeNumbers():
    prime[0] = prime[1] = False
    i = 2
    while i ** 2 < n:
        if prime[i]:
            j = i**2
            while j <= n:
                prime[j] = False
                j += i
        i += 1


def pre():
    count = 0
    for i in range(1, n+1):
        if prime[i]:
            count += 1
        prefix[i] = count


def totalComponents(m):
    if 2 <= m <= 3:
        return m-1
    return prefix[m]-prefix[m//2]+1


if __name__ == '__main__':

    t = int(input())
    a = [0]*t
    for i in range(t):
        a[i] = int(input())
    n = max(a)
    prime = [True]*(n+1)
    prefix = [0]*(n+1)
    primeNumbers()
    pre()
    for i in range(t):
        print(totalComponents(a[i]))
