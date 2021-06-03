from heapq import heappush, heappop
arr = []
killed = []
n, v = list(map(int, input().split()))
for _ in range(n + v):
    k = int(input())
    if k == -1:
        killed.append(heappop(arr))
        continue
    heappush(arr, -k)
[print(i * -1) for i in killed]


## partially Accepted solution due to TLE

# n,m = map(int,input().split())
# arr = []
# ans = []
# count = 0
# for c in range(n+m):
#     if count==m:
#         break
#     num = int(input())
#     if num==-1:
#         ans.append(max(arr[:c]))
#         arr.remove(max(arr[:c]))
#         count+=1
#     else:
#         arr.append(num)
# print(*ans,sep="\n")



