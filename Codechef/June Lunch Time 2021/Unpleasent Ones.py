testcase=int(input())
while testcase!=0:
    testcase-=1
    total_nums=int(input())
    odd_items=[]
    even_items=[]
    arr=list(map(int,input().split()))
    for ele in arr:
        if ele % 2 == 0:
            even_items.append(ele)
        else:
            odd_items.append(ele)

    print(*(even_items+odd_items))
