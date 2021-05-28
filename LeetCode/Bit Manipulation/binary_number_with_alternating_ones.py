## optimized but manipulation code

"""
Alternating bits appear after specific intervals.
If the current number (say n) which has alternating bits is an odd number, then the next number 
with alternating bits wil be (2 * n).

If the current number (n) which has alternating bits is an even number, then the next number 
with alternating bits will be (2 * n + 1).
"""
def hasAlternatingBits(n):
    res = 0
    while n > res:
        if (res & 1) == 0:
            res <<= 1
            res += 1
        else:
            res <<= 1
            
    return res == n

hasAlternatingBits(4)
## my way easy but long

def hasAlternatingBits(n):
    n = bin(n).replace("0b","")
    i=0
    if n[0]=='1':
        i=1
        while i!=len(n):
            if i%2==1:
                if n[i] != '0':
                    return False
                i+=1
                continue
            if i%2==0:
                if n[i] != '1':
                    return False
                i+=1
                continue
        return True
    if n[0]=='0':
        i=1
        while i!=len(n):
            if i%2==1:
                if n[i]=='1':
                    continue
                else:
                    return False
            if i%2==0:
                if n[i]=='0':
                    continue
                else:
                    return False
        return True

print(hasAlternatingBits(4))