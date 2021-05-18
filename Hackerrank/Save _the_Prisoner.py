def saveThePrisoner(n, m, s):
    ans = ( s + m - 1 )%n
    if ans == 0:
        ans = n
    return ( ans )