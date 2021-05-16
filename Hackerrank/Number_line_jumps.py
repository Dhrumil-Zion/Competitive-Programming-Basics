def kangaroo(x1, v1, x2, v2):
    for y in range(10000):
        if x1 + y * v1 == x2 + y * v2:
            return "YES"
    return "NO" 
    
re = kangaroo(14,4,98,2)    
de = kangaroo(0,2,5,3)
ee = kangaroo(0,3,4,2)    

print(re)
print(de)
print(ee)

