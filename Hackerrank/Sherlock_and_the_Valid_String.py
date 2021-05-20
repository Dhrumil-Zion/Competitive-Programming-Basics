from collections import Counter
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