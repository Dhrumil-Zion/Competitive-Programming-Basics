T = int(input())
count = 0
temp = 0
while T!=0:
    input_data = int(input())
    count=1
    if input_data in [1, 2]:
        print(count)
        break
    temp = 2
    while temp < input_data:
        count+=1
        temp = (temp+1)*2
    print(count)
    T-=1