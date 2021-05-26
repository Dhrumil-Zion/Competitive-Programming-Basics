# https://www.codechef.com/LETS2021/problems/LETSC001
def primecount(n):
    prime = [True]*(n+1)
    i = 2
    while i*i <= n:
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j] = False
        i += 1
    primenumbercount = 0
    for j in range(2, n+1):
        if prime[j]:
            primenumbercount += 1
    return primenumbercount


if __name__ == '__main__':
    n = int(input())
    print(primecount(n))
