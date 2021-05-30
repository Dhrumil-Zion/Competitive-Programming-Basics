T =int(input())
while T!=0:
    no_of_users,no_of_admins,no_of_test = map(int,input().split())
    test_rescords = list(map(int,input().split()))
    disqualification = [
        c
        for c in set(test_rescords)
        if test_rescords.count(c) > 1 and  1<=c<=no_of_users
    ]
    print(len(disqualification),*disqualification)
    T-=1

# T =int(input())
# while T!=0:
#     no_of_users,no_of_admins,no_of_test = map(int,input().split())
#     id = list(map(int,input().split()))
#     repeatedId = set()
#     userid = set()
#     for i in id:
#         if 1 <= i <= no_of_users:
#             if i in userid:
#                 repeatedId.add(i)
#             userid.add(i)
#     print(len(list(repeatedId)),*list(repeatedId))
#     T-=1