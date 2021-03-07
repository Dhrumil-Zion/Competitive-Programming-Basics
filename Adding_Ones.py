"""
link = "https://practice.geeksforgeeks.org/problems/adding-ones3628/1#"
"""

c = [0,0,0]             ##### Optimized code for below program
updates = [1,1,2,3]
k = 4
n = 3
i = 0
while (i<k):
    c[updates[i]-1] +=1
    i +=1
i = 1    
while (i<n):
    c[i]+=c[i-1]
    i +=1
print(c)


inp1 = [int(x) for x in input().split()]
inp2 = [int(x) for x in input().split()]
l1 = inp1[0] + 1
l2 = inp1[1]
final_arr = inp2[:l2]
arr  = []
count = 0

for x in range(l1):
    arr.append(0)
for y in final_arr:
    for x in range(1,l1):
        if y <= x:
            arr[x] +=1
arr.pop(0)
print(arr)           
