T = int(input())
arr = []
while T!=0:
    arr.append(int(input()))
    T-=1
arr.sort()
print(*arr,sep="\n")