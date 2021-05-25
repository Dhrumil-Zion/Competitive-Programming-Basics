n=5
temp=[]
for c in range(n+1):
    h = bin(c)[2:]
    temp.append(h.count('1'))
print(temp)

def countBits(n):
    if n == 0:
        return [0]
    if n==1:
        return [0,1]
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        print(i)
        dp[i] = dp[i>>1] if i%2==0 else dp[(i-1)>>1]+1
        print(dp[i])
        print(dp)
    return dp
countBits(10)