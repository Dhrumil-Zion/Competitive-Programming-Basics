# Problem Name: Range Odd 
# Problem Code: RNGEODD

l,r = input().split()
temp = [v for v in range(int(l),int(r)+1) if v%2!=0]
temp.sort()
print(" ".join(str(c) for c in temp))