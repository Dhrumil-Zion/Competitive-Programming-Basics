# # # # # z = [x for x in input().split()]

# # # # # if len(z)>1:
# # # # #     withdraw = int(z[0])
# # # # #     old_bal = int(z[1])
# # # # #     bal = float(z[1])
# # # # #     if withdraw == old_bal:
# # # # #         print("{:.2f}".format(bal))
# # # # #     elif withdraw % 5 !=0:
# # # # #         print("{:.2f}".format(bal))
# # # # #     elif withdraw > old_bal:
# # # # #         print("{:.2f}".format(bal))  
# # # # #     elif withdraw < old_bal and withdraw %5 == 0:
# # # # #         bal = bal - float(z[0]) - float(0.50)
# # # # #         print("{:.2f}".format(bal))


# # # # # Python3 code to demonstrate
# # # # # getting numbers from string
# # # # # using List comprehension + isdigit() +split()

# # # # # initializing string
# # # # test_string = "abc123askdj"

# # # # z = [x for x in test_string]
# # # # print(z[2].isdigit())
# # # T = int(input())
# # # while T:
# # #     a = []
# # #     string = input()
# # #     z = [x for x in string]
# # #     for x in z:
# # #         if x.isdigit():
# # #             a.append(int(x))
# # #     print(sum(a))
# # #     T-=1
# # st  = "ashmdvbsajhdjahsvkdyhsa"
# # print(len(set(st)))

# lower = 1
# upper = 10

# print("Prime numbers between", lower, "and", upper, "are:")

# for num in range(lower, upper + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)

a, b, i, j, flag = 0, 0, 0, 0, 0
 
a = int(input())
b = int(input())
for i in range(a, b + 1):
    if (i == 1):
        continue
    flag = 1
    
    for j in range(2, i // 2 + 1):
        if (i % j == 0):
            flag = 0
            break

    if (flag == 1):
        print(i)