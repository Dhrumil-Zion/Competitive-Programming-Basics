# Problem Name: Find Second Largest 
# Problem Code: SECLAR
num1 = int(input())
num2 = int(input())
num3 = int(input())
s = [num1,num2,num3]
s.sort()
print(s[-2])