n = 7
one =1
two = 2
three = 3
print(one,two,three)
for c in range(3,n):
    temp = one+two+three
    print(temp)
    one = two 
    two = three
    three = temp