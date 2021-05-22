s = "codeleet"
indices =[4,5,6,7,0,2,1,3]
output = list(s)
for i in range(len(s)):
    output[indices[i]] = s[i]    
print(''.join(output))