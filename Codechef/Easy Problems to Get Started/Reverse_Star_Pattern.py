# Problem Name: Reverse Star Pattern 
# Problem Code: REVSTRPT

num = int(input())
for n in range(1,num+1):
    l = " "*(num-1)
    l += "*" * n
    print(l)
    num-=1