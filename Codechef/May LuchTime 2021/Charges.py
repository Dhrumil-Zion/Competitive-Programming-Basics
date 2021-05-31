# # sourcery skip: assign-if-exp, sum-comprehension
# T=int(input())
# while T!=0:
#     N,K =map(int,input().split())
#     st = list(input())
#     arr = list(map(int,input().split()))
#     for c in arr:
#         count=0
#         if st[int(c)-1]=='0':
#             st[int(c)-1]='1'
#         else:
#             st[int(c)-1]='0'
#         for v in range(1,len(st)):
#             if st[v-1]==st[v]:
#                 count+=2
#             else:
#                 count+=1
#         print(count)
#     T-=1

def charges(m, a, st, Q):
    if m == 1:
        print(0)
        return
    length = 0
    for x in range(1, m):
        if st[x - 1] == st[x]:
            length += 2
        else:
            length += 1

    for x in range(0, a):
        pos = Q[x] - 1
        if pos == 0 and m > 1:
            if st[pos] == st[pos + 1]:
                length -= 1
            else:
                length += 1
            print(length)
            if st[pos] == 0:
                st[pos] = 1
            else:
                st[pos] = 0
            continue
        if pos == m-1 and m > 1:
            if st[pos] != st[pos - 1]:
                length += 1
            else:
                length -= 1
            print(length)
            if st[pos] == 0:
                st[pos] = 1
            else:
                st[pos] = 0
            continue
        if st[pos] != st[pos + 1]:
            length += 1
        else:
            length -= 1
        if st[pos] != st[pos - 1]:
            length += 1
        else:
            length -= 1
        if st[pos] == 0:
            st[pos] = 1
        else:
            st[pos] = 0
        print(length)