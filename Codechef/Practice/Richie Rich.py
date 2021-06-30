testcase = int(input())
while testcase!=0:
    A,B,X = map(int,input().split())
    count = 0
    while A!=B:
        count+=1
        A+=X
    print(count)
    testcase-=1
