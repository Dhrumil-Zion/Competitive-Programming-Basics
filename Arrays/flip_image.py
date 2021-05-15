image = [[1,1,0],[1,0,1],[0,0,0]]
temp=[]
for c in image:
    c=c.reverse()
for c in range(len(image)):
    for d in range(len(image[c])):
        image[c][d] = 0 if image[c][d]==1 else 1
print(image)