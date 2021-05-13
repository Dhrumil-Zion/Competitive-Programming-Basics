from collections import Counter
a = "abcc"
# temp = [a.count(c) for c in set(a)]
# temp.sort()
# c = list(set(temp))
# if len(c)==1:
#     print("YES")
# elif len(c)==2:
#     if abs(c[0]-c[1])==1:
#         if temp.count(c[0])==len(temp)-1 or temp.count(c[1])== len(temp)-1:
#             print("YES")
#         else:
#             print("NO")
#     else:
#         print("NO")
# else:
#     print("NO")

def isValid(s):
    c = Counter(s)
    freq = Counter(c.values())
    if len(freq) == 1:
        return "YES"
    elif len(freq) == 2:
        key_max = max(freq.keys())
        key_min = min(freq.keys())
        if key_max - key_min == 1 and freq[key_max] == 1:
            return "YES"
        elif key_min == 1 and freq[key_min] == 1:
            return "YES"
    return "NO"
print(isValid(a))