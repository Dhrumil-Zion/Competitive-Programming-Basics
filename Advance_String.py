from math import pow

def subString(s):
    n = len(s)
    d = []
    for i in range(n):
        for le in range(i+1,n+1):
            d.append(s[i: le])
    final = list(set(d))
    print(final)
    eq=0
    for x in final:
        length = len(x)
        disticnt_char = len(set(x))
        eq += pow(length,disticnt_char)%100000007

    return int(eq%100000007)

s = "ddddddddddddddddddeeeeeeeeeeeeeeeeeeiiiiiiiiiiiiiiiiiiyyyyyyyyyyyyyyyyyyiyd"
ans = subString(s)
print(ans)

