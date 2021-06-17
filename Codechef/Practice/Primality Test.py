import math
def prime(n):
    if(n==1):
        return 'no'
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return 'no'
    return 'yes'
for _ in range(int(input())):
    ans=prime(int(input()))
    print(ans)