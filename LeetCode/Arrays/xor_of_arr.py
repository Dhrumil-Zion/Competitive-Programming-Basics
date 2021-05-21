from functools import reduce
n=10
start=5
test_list = []
i=0
while n!=0:
    test_list.append(start + 2*i)
    i+=1
    n-=1

print(reduce(lambda x, y: x ^ y, test_list)) 
