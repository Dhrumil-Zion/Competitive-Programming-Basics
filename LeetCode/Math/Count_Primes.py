def countPrimes(n):
    if n in [0,1,2]:
        return 0
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return len([2] + [i for i in range(3,n,2) if sieve[i]])

print(countPrimes(100))