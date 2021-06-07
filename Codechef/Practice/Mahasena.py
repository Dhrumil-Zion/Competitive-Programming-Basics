T = int(input())
m=list(map(int,input().split()))
t = 0
r = 0
for i in (m):
    if i%2==0:
        t+=1
    else:
        r+=1
if t>r:
    print("READY FOR BATTLE")
else:
    print("NOT READY")