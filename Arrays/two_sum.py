a = [3,3]
k = 6
if len(a)==2:
    print(a)
for f in range(len(a)):
    for g in range(f+1,len(a)):
        if a[f]+a[g] == k:
            print([f,g])
