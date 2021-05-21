coordinates = "c7"
letters = ['a','b','c','d','e','f','g','h']
if letters.index(coordinates[0])%2==0 and int(coordinates[-1])%2==0:
    print("yes")
elif letters.index(coordinates[0])%2!=0 and int(coordinates[-1])%2!=0:
    print("yes")
else:
    print("no")