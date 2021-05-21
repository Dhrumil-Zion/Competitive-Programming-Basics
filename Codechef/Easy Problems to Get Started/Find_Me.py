# Problem Name: Find Me 
# Problem Code: FINDMELI

l,k =input().split()
nums = [int(c) for c in input().split()]
if int(k) in nums[:int(l)]:
    print(1)
else:
    print(-1)