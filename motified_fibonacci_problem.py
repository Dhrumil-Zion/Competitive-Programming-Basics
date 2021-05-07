n = 7
one =1
two = 2
three = 3
tempp = [one, two, three]
for _ in range(3,n):
    temp = one+two+three
    tempp.append(temp)
    one = two 
    two = three
    three = temp

print(tempp)