a =[
    [10,20,30], 
    [5,10,20],
    [2,4,6]
    ]
p =[
    [0,0,0], 
    [0,0,0],
    [0,0,0]
    ]

for x in range(3):
    for y in range(3):
        print(a[x][y],end=" ")
    print("") 
       
for x in range(3):
    for y in range(3):
        if x == 0 and y ==0:
            p[x][y] = a[x][y]
        elif x == 0 and y > 0:    
            for z in range(y):
                p[x][y] = p[x][y]+a[x][z]
        elif x > 0 and y ==0:
            for z in range(x):
                p[x][y] = p[x][y]+a[z][y]
        elif x>0 and y>0:
            for z in range(y):
                p[x][y] = p[x][y]+a[x][z]
            for z in range(x):
                p[x][y] = p[x][y]+a[z][y]    

for x in range(3):
    for y in range(3):
        print(p[x][y],end=" ")
    print("") 
