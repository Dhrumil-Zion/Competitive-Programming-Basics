testcase =int(input())
while testcase!=0:
    apples,oranges,money =map(int,input().split())
    print(0) if abs(apples-oranges)<=money else print(abs(apples-oranges)-money)
    testcase-=1


## fuzzy logic 

# testcase =int(input())
# while testcase!=0:
#     apples,oranges,money =map(int,input().split())
#     flag =0
#     if apples==oranges:
#         print(0)
#     elif apples>oranges:
#         for _ in range(money):
#             oranges+=1
#             if apples==oranges:
#                 print(0)
#                 flag=1
#                 break
#         if flag==0:
#             print(apples-oranges)
#     else:
#         for _ in range(money):
#             apples+=1
#             if apples==oranges:
#                 print(0)
#                 flag=1
#                 break
#         if flag==0:
#             print(oranges-apples)
#     testcase-=1