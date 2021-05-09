# import itertools
# n = str(1001)
# c =0
# li = []
# for pair in itertools.combinations([c for c in range(1,9)],2):
#     # if sum(pair)<=int(n,2):
#     #     c+=1
#     # li.append(pair)
#     print(pair)
# print(len(li))


from itertools import product
intt = int(input())
n=input()
n= n[:intt]
K = 2
temp = [list(range(1, int(n,2)+1)) for _ in range(K)]
res = list(product(*temp))
k = sum(r[0]+r[1]==r[0]^r[1] for r in res)
print("{}".format(k%((10**9)+7)))
