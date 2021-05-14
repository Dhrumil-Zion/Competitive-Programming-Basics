s = "abcabcbb"

## Optimized one

queue = []
queueDict = {}
maxLen = 0

for char in s:
    while char in queueDict:
        k = queue.pop(0)
        queueDict.pop(k)
    queue.append(char)
    queueDict[char] = char
    queueLen = len(queue)
    if queueLen > maxLen:
        maxLen = queueLen
        
print(maxLen)


## TLE but working 


# n=len(s)
# m = 0
# for i in range(n):
#     temp=""
#     for j in range(i,n):
#         temp+=s[j]
#         if len(temp)==len(set(temp)):
#             if len(temp)>m:
#                 m=len(temp)
# print(m)
