# def findDigits(n):
#     t=n
#     c=0
#     while n!=0:
#         temp = n%10
#         n=int(n/10)
#         if temp ==0:
#             continue
#         if t%temp==0:
#             c+=1
#     return c

# ans = findDigits(1012)    
# print(ans)


# def marsExploration(s):
#     l =['S','O','S']
#     c=0
#     k = 0
#     string = [str(x) for x in s]
#     le = len(string)
#     while k!=le:
#         i = 0 
#         while i!=3:
#             if l[i]!=string[k]:
#                 c+=1
#                 i+=1
#                 k+=1
#             else:
#                 i+=1
#                 k+=1
#     print(c)

# s="SOSSOSSOS"

# marsExploration(s)


# Complete the caesarCipher function below.
def caesarCipher(s, k):
    k = k% 26
    l = list(s)
    e = []
    for item in l:
        z = ord(item)
        if (z >= 97 and z<=122):
            if (z+k) > 122:
                e.append(chr(96 + (z+k-122)))
            else:
                e.append(chr(z+k))
        elif (z>=65 and z<=90):
            if (z+k) > 90:
                e.append(chr(64 + (z+k-90)))
            else:
                e.append(chr(z+k))
        else:
            e.append(item)
    print("".join([x for x in e]))


s ="middle-Outz"
k=3 
caesarCipher(s,k)   
