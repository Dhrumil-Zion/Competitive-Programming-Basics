s ="RLRRLLRLRL"
n =len(s)
count=0
c = []
for i in range(n):
    temp=""
    for j in range(i,n):
        temp+=s[j]
        if temp.count('R')==temp.count('L'):
            count+=1
            c.append(temp)
print(set(c))