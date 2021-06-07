for _ in range(int(input())):
    n1,n2 =map(int,input().split())
    if n1>n2:
        print(">")
    elif n1==n2:
        print("=")
    else:
        print("<")