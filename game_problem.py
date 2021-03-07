"""
Problem Link = https://www.hackerrank.com/challenges/an-interesting-game-1/problem
"""

def gamingArray_optimized(arr):
    count=0 
    m=0 
    for i in arr:
        if i>m:
            m=i
            count+=1
    if count%2==0:
        print("ANDY")
    else:
        print("BOB")


def gamingArray(arr):       ### time exceeding for 4 cases , optimizationx please
    c = -1
    while(1):
        if len(arr) == 0:
            break
        i = arr.index(max(arr))
        del arr[i:]
        c +=1
    
    if c % 2==0:
        print("BOB")
    else:
        print("ANDY")    
    

t =[7 ,4 ,6 ,5 ,9]     ## ANDY
s = [1, 3, 5, 7, 9]    ## BOB
e = [5 ,2 ,6 ,3 ,4]   ## ANDY
d = [3,1]             ## BOB  
gamingArray(t)
gamingArray(s)
gamingArray(e)
gamingArray(d)    
gamingArray_optimized(t)
gamingArray_optimized(s)
gamingArray_optimized(e)
gamingArray_optimized(d)