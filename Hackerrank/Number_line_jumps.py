def kangaroo(x1, v1, x2, v2):
    for y in range(10000):
        if x1 + y * v1 == x2 + y * v2:
            return "YES"
    return "NO" 