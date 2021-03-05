a = [1,2,3,1,3,5,6,1,2,5,3,7,8,4,2,7,9,4,5,2,1,5,2,3,7,8,4]
x = set(a)
for y in x:
    print("{} - {} times".format(y,a.count(y)))