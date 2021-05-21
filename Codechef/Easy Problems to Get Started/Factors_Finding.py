# Problem Name: Factors Finding
# Problem Code: DIFACTRS

num = int(input())
count=0
temp = []
for c in range(1,num+1):
    if num%c==0:
        count+=1
        temp.append(c)
temp.sort()
c= [str(n) for n in temp]
print(count)
print(" ".join(c))