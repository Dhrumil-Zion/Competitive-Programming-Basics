def birthday(s, d, m):
    tp = (len(s)-m) + 1 
    return len([1 for i in range(tp) if sum(s[i:i+m])==d])

s = [1 ,2 ,1 ,3 ,2]
d = 3 
m = 2

print(birthday(s,d,m))