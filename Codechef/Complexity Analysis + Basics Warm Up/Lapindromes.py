# Problem Name: Lapindromes 
# Problem Code: LAPIN

testcase = int(input())
while testcase >0 :
    input_string = input()
    length = len(input_string)
    if length % 2 == 0 :
        left_side = input_string[:length//2]
        right_side = input_string[length//2:]
    else :
        left_side = input_string[:(length-1) // 2]
        right_side = input_string[(length+1) // 2:]
    if sorted(left_side) == sorted(right_side) :
        print("YES")
    else :
        print("NO")
    testcase -= 1


## Approach 2 

t = int(input())
while t>0:
    input_string = input()
    L = list(input_string)
    length = len(L)
    index = length//2
    first_half = L[:index]
    second_half = L[-index:]
    first_half.sort()
    second_half.sort()
    if first_half==second_half:
        print("YES")
    else:
        print("NO")
    t-=1