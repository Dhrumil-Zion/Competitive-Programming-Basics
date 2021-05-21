# Problem Name: Valid Triangle Or Not 
# Problem Code: TRIVALCH

side1,side2,side3 = map(int, input().split())

if (side1+side2)>=side3 and (side2+side3)>=side1 and side1+side3>=side2:
    print('YES')
else:
    print('NO')