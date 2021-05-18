def repeatedString(s, n):
    x = (n//len(s))
    y = n%len(s)
    c = s.count('a')
    ans = c * x
    for z in range(y):
        if s[z]=='a':
            ans +=1
    return ans