l = [ 2,4,2,6,1,7,8,9,2,1]
n=len(l)
z=[1 for i in l]
for i in range(n-1):
    if l[i]>l[i+1]:
        if z[i]<=z[i+1]:
            z[i]=z[i+1]+1
    elif l[i]<l[i+1]:
        if z[i+1]<=z[i]:
            z[i+1]=z[i]+1
print(sum(z))  