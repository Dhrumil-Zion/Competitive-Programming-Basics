## most optimized one

def sumOddLengthSubarrays(arr):
    res = 0; freq = 0; n = len(arr)
    for i in range(n):
        freq = freq-(i+1)//2+(n-i+1)//2
        res += freq*arr[i]
    return res

def sub_lists (arr):
    k=0
    for i in range(len(arr) + 1):
        for j in range(i):
            if len(arr[j: i])%2!=0:
                k+=sum(arr[j: i])
    return k

l1 = [10,11,12]
print(sub_lists(l1))
