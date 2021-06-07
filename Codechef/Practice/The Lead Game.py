win=''
winP=0
p1=0
p2=0
for _ in range(int(input())):
    a,b=map(int,input().split())
    p1+=a
    p2+=b
    if p1>p2 and p1-p2>winP:
        winP=p1-p2
        win='1'
    if p2>p1 and p2-p1>winP:
        winP=p2-p1
        win='2'
print(win,winP)