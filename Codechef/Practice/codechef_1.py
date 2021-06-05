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