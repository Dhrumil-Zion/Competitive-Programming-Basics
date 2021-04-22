L = [-2,-3,4,-1,-2,1,5,-3]
arr = [L[i:i+j] for i in range(len(L)) for j in range(1,len(L)-i+1)]
z = [sum(c) for c in arr]
print(max(z))