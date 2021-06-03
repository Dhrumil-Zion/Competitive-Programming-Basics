from collections import Counter
ans = []
c = 0
a, b, c = list(map(int, input().split()))
d = [int(input()) for _ in range(a + b + c)]
counter = Counter(d)
for voterId, fre in counter.items():
    if fre > 1:
        ans.append(voterId)
        c += 1
ans.sort()
print(c)
print(*ans,sep="\n")

# d = {}
# a, b, c = list(map(int, input().split()))
# for _ in range(a + b + c):
#     k = int(input())
#     if k in d:
#         d[k] += 1
#     else:
#         d[k] = 1
# nl = []
# c = 0
# for k, v in d.items():
#     if v > 1:
#         nl.append(k)
#         c += 1
# nl.sort()
# print(c)
# for i in nl:
#     print(i)