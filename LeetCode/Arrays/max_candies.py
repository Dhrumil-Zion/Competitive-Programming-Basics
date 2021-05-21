candies = [12,1,12]
extraCandies = 10
k = max(candies)
temp = []
for c in candies:
    if c+extraCandies >=k:
        temp.append(True)
    else:
        temp.append(False)
print(temp)