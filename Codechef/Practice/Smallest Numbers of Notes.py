T = int(input())
a = [100, 50, 10, 5, 2, 1]
for _ in range(T):
    n = int(input())
    b = 0
    for x in a:
        if (x <= n):
            b += n // x
            n %= x
    print(b)