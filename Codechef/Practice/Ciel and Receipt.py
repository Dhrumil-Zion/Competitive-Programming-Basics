t=int(input())
menu=[2048,1024,512,256,128,64,32,16,8,4,2,1]
for _ in range(t):
    p = int(input())
    n = 0
    ans=0
    while n < 12:
        ans += p//menu[n]
        p %= menu[n]
        if p==0:
            break
        n += 1
    print(ans)