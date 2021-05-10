from itertools import product
intt = int(input())
n=input()
n= n[:intt]
K = 2
temp = [list(range(1, int(n,2)+1)) for _ in range(K)]
res = list(product(*temp))
k = sum(r[0]+r[1]==r[0]^r[1] for r in res)
print("{}".format(k%((10**9)+7)))



# from itertools import combinations
# def solution(N, S):
#     DecimalofS = int(S, 2)
#     elements = [i for i in range(1, DecimalofS + 1)]
#     pairs = set()
#     for i in elements:
#         for j in elements:
#             pairs.add((i, j))
#     count = 0
#     for pair in pairs:
#         if pair[0] + pair[1] == pair[0] ^ pair[1]:
#             count += 1
#     print(count)


# N = int(input())
# S = input()
# solution(N, S)