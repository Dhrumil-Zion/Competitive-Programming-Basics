def funnyString(s):
    a = []
    b= []
    p = []
    c= []
    sd = s[::-1]
    for x in range(len(s)):
        a.append(ord(s[x]))
        b.append(ord(sd[x]))
    for x in range(len(a)-1):
        p.append(abs(a[x]-a[x+1]))
        c.append(abs(b[x]-b[x+1]))
        
    if p==c:
        return "Funny"
    else:
        return "Not Funny"