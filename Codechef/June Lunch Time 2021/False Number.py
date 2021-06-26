t= int(input())
while t!=0:
    number = list(input())
    if int(number[0])>1:
        number.insert(0,'1')
    else:
        number.insert(1,'0')
    print(int("".join(number)))
    t-=1