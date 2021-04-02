def luckBalance(k, contests):
    a = []
    b = []
    for x in contests:
        if x[1] == 1:
            a.append(x[0])
        else:
            b.append(x[0])
    a.sort()
    print("{} value of k and {} value of len(a) and {} may be the ans".format(k,len(a),sum(b)+sum(a)))

    if k > len(a):
        return sum(a)+sum(b)
    return sum(a[len(a)-k:]) + sum(b) - sum(a[:len(a)-k])
        

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    print(result)