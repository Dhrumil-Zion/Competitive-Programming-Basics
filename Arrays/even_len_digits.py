nums = [1,12,322,1233213,2131243,123213,32523,436543,4234,546985]
count = sum(len(str(c))%2==0 for c in nums)
print(count)