T = int(input())
while T!=0:
    num_len,first,second =map(int,input().split())
    num_list = [first, second]
    while len(num_list) < num_len:
        num_list.append(sum(num_list)%10)
    if sum(num_list)%3==0:
        print("YES")
    else:
        print("NO")
    T-=1