arr = [3,1,7,11]
flag = 0
for a in arr:
    temp = a*2
    if temp in arr:
        flag=1
        print("True")
if flag==0:        
    print("false")
