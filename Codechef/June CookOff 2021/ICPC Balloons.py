t = int(input())
while t!=0:
    n = int(input())
    count =0
    ans=-1
    difficulties  = list(map(int,input().split()))
    for id in range(len(difficulties)):
        if difficulties[id]<=7:
            count+=1
        if count==7:
            ans = id+1
            count+=1
    print(ans)
    t-=1