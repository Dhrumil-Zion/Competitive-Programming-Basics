## https://www.hackerrank.com/challenges/save-the-prisoner/problem


## final code 

total_num = 4
total_candy = 3
starting_point = 2

ans = ( starting_point + total_candy - 1 )%total_num
if ans == 0:
    ans = total_num
print( ans )

## not all test cases are covered 

total_num = 4
total_candy = 3
starting_point = 2


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