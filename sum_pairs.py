## https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

ar = [1,2,3,4,5,6]
k = 5
temp = []
for c in range(len(ar)):
    for g in range(c,len(ar)):
        if c < g and (ar[c]+ar[g]) % k == 0:
            temp.append([ar[c],ar[g]])
print(len(temp))


## optimized code

count = 0
for i in range(len(ar)-1):
    j = i+1
    while j < len(ar):
        if ((ar[i] + ar[j]) % k) == 0:
            count += 1
        j += 1
print(count)

## optimized code


pairs = [(ar[i], ar[j]) for i in range(len(ar)) for j in range(len(ar)) if i < j]
print(sum(1 if (pair[0] + pair[1]) % k == 0 else 0 for pair in pairs))