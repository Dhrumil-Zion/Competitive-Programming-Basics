# First line will contain T, number of testcases.
# Second line contain two integers N,K.
# Third line contain N number i.e. the array element

T = int(input())
while T!=0:
    N,K =map(int,input().split())
    arr = list(map(int,input().split()))
    temp =[]
    for c in range(1,K):
        flg =0
        for v in arr:
            if c%v==0:
                continue
            else:
                flg=1
        if flg==0:
            temp.append(c)
    print(len(temp))
    T-=1