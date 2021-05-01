## https://www.hackerrank.com/challenges/save-the-prisoner/problem

total_num = 57109959
total_candy = 451440582
starting_point = 4188603


print((starting_point+total_candy%total_num)-1)
if (total_candy%total_num) + starting_point > total_num:
    print((total_candy%total_num) - (total_num-starting_point)-1)
if total_num == total_candy:
    print(total_num)

# temp = []
# for f in range(total_candy):
#     if starting_point == total_num:
#         temp.append(starting_point)
#         starting_point = 1
#         continue
#     temp.append(starting_point)
#     starting_point+=1

# print(temp[-1])