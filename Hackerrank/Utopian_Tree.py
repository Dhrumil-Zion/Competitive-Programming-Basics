def utopianTree(n):
    y = 1
    z=1
    if n ==0:
        z = z
    else:
        for x in range(n):
            if x%2==0:
                z *= 2
            else:
                z += 1

    return z