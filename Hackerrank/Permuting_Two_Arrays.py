def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)
    if (any(a+b<k for a,b in zip(A,B))):
        return "NO"
    else:
        return "YES"