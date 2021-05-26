T = int(input())
while T!=0:
    st =input()
    temp = list(set(st))
    if ('E' in temp) and ('e' in temp):
        if 'C' in temp and 'o' in temp and 'D' in temp:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    T-=1