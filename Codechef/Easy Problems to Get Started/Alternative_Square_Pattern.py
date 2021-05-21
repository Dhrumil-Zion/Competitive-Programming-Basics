# Problem Name: Alternative Square Pattern 
# Problem Code: SQALPAT

num_of_lines = int(input())

## alternate the things to print with alternate reverse function to list

for i in range(1,num_of_lines+1):
    start=(i*5)-4
    lst=[e for e in range(start,start+5)]
    if i%2==1:
        print(*lst)
    if i%2==0:
        lst.reverse()
        print(*lst)