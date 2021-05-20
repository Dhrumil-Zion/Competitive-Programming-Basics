def balancedSums(arr):
    s = sum(arr)
    left = 0
    for i in arr:
        if left == s-left-i:
            return "YES"
        left += i
    return "NO"