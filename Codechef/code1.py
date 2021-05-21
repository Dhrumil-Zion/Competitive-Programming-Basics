n = int(input())
starting = 3
temp = [True] * n
for i in range(starting,int(n**0.5)+1,2):
    if temp[i]:
        temp[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
print( [2] + [i for i in range(3,n,2) if temp[i]])

