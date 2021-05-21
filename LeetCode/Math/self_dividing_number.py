left = 1
right = 22
temp=[]
if right<10:
    ans = [c for c in range(left,right+1)]
    print(ans)
else:
    for c in range(left,right+1):
        if '0' in str(c):
            continue
        flag=1
        v =str(c)
        for k in range(len(v)):
            if c%int(v[k])==0:
                continue
            flag=0
            break
        if flag==1:
            temp.append(c)
print(temp)


## some what faster thab above code

u=[]
for i in range(left , right+1):
    p=str(i)
    h=0
    if '0' not in p:
        for j in p:
            if i%int(j)!=0:
                h=1
                break
    else:
        h=1
    if h==0:
        u.append(i)        
print(u)