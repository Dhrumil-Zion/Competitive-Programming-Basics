t =int(input())
while t!=0:
    n = int(input())
    s = input()
    if 'I' in s:
            print('INDIAN')
    elif 'Y' in s:
        print('NOT INDIAN')
    else:
        print('NOT SURE')
    t-=1