## https://www.geeksforgeeks.org/convert-an-array-to-reduced-form-set-1-simple-and-hashing/

ar = (1,2,5,3)
arr =list(ar)
arr.sort()
z = [arr.index(ar[c]) for c in range(len(arr))]
print(z)
