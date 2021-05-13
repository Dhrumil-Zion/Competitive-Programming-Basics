nums = [0,1]
even = []
odd = []
for v in nums:
    if v%2==0:
        even.append(v)
    else:
        odd.append(v)
print(even+odd)
