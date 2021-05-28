
## optimized code 

def totalHammingDistance(nums):
    len_nums = len(nums)
    total_hamming_distance = 0
    for shift in range(30):
        mask = 1 << shift
        ones = sum(bool(num & mask) for num in nums)
        zeros = len_nums - ones
        total_hamming_distance += zeros * ones
    return total_hamming_distance
print(totalHammingDistance([2,4,14]))


## TLE code , slower but easy to understand

import itertools
s = [4,14,2]
n=2
m = itertools.combinations(s, n)
count = 0
for x,y in m:
    while x or y:
        if x & 1 != y & 1:
            count += 1
        x = x >> 1
        y = y >> 1
print(count)
