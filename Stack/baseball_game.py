ops = ["1"]
arr = []
for o in ops:
    if o=="C":
        arr.pop()
    elif o=="D":
        arr.append(arr[-1]*2)
    elif o=="+":
        arr.append(arr[-1]+arr[-2])
    else:
        arr.append(int(o))
print(arr)