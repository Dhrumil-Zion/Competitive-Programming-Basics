import random
def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)
    if (any(a+b<k for a,b in zip(A,B))):
        return "NO"
    else:
        return "YES"

A =[84 ,2 ,50 ,51 ,19, 58, 12 ,90 ,81 ,68 ,54 ,73 ,81 ,31 ,79 ,85 ,39 ,2]
B =[53 ,102, 40 ,17 ,33 ,92 ,18 ,79 ,66 ,23 ,84 ,25 ,38 ,43, 27, 55, 8, 19]
K =94

print(twoArrays(K,A,B))


# def twoArrays(k, A, B):
#     flg2=0
#     for _ in range(500):
#         for c in range(len(A)):
#             if A[c]+B[c]>=k:
#                 continue
#             flg2=1
#             break
#         if flg2==0:
#             return "YES"
#         flg2=0
#         random.shuffle(A)
#     return "NO"