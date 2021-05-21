tempratures= [55,38,53,81,61,93,97,32,43,78]

result=[0]*len(tempratures)
stack = []
for idx, currentTemp in enumerate(tempratures):
    while stack and tempratures[stack[-1]] < currentTemp:
        prevIdx = stack.pop()
        result[prevIdx] = idx - prevIdx
    stack.append(idx)
print(result)