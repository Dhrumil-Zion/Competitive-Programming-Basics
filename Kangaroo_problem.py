"""
link = https://www.hackerrank.com/challenges/kangaroo/problem
"""
def kangaroo_optimization(x1, v1, x2, v2):
    y=0
    while (y<10000):
        if x1 + y * v1 == x2 + y * v2:
            return "YES"
        y+=1
    return "NO"          
             

def kangaroo(x1, v1, x2, v2):
    diff1 =v1
    diff2 = v2
    k=0
    flag = 0
    while k<10000:
        if (x2 > x1 and v2>v1) or (x1>x2 and v1>v2):
            return "NO"
            break
        a = x1+v1
        b = x2+v2
        if a==b:
            return "YES"
            break
        v1 = v1 + diff1
        v2 = v2 + diff2
        if k == 9999:
            flag=1 
        k+=1    
    if flag ==1:
        return "NO"   

# re = kangaroo(14,4,98,2)    
# de = kangaroo(0,2,5,3)
# ee = kangaroo(0,3,4,2)        
re = kangaroo_optimization(14,4,98,2)    
de = kangaroo_optimization(0,2,5,3)
ee = kangaroo_optimization(0,3,4,2)        

print(re)
print(de)
print(ee)