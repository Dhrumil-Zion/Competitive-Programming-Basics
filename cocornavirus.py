v =input()
nu = int(input())
an = []
n = len(v)
while nu!=0:
    j = 0
    i = 0
    d =input()
    m = len(d)
    while j < m and i < n:
        if d[j] == v[i]:
            j += 1
        i += 1
    if j == m:
        an.append("POSITIVE")
    else:
        an.append("NEGATIVE")
    nu-=1

print(*an,sep='\n')
