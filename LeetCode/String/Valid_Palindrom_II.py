def validPalindrome(self, s: str) -> bool:
    j=len(s)-1
    for i in range(j):
        if s[i]!=s[j]:
            x=s[0:i]+s[i+1:]
            y=s[0:j]+s[j+1:]
            return x == x[::-1] or y == y[::-1]
        j-=1
    return True