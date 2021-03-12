"""
link = https://www.hackerrank.com/challenges/electronics-shop/problem
"""

def getMoneySpent(keyboards, drives, b):
    if len(keyboards) == 1:
        if keyboards[0]>=b:
            return -1
    if len(drives) ==1:
        if drives[0]>=b:
            return -1
    n = []            
    for x in keyboards:
        for y in drives:
            temp = x+y
            if temp>b:
                continue
            else:
                n.append(temp)
    if len(n)==0:
        return -1            
    return max(n)  

b=10
k=[3,1]
d=[5,2,8]
ans = getMoneySpent(k,d,b)
print(ans)