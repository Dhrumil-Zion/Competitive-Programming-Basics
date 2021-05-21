from typing import Counter


n = int(input())
sweets =0
count=0
while sweets<n:
    sweets =(sweets+1)*2
    print(sweets)
    count+=1
print(count)
