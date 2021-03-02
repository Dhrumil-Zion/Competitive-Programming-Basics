"""
Count of n digit numbers whose sum of digits equals to given sum
Input:  n = 2, sum = 2
Output: 2
Explanation: Numbers are 11 and 20

Input:  n = 2, sum = 5
Output: 5
Explanation: Numbers are 14, 23, 32, 41 and 50
"""

def processing(n,sum,arr):
    temp = 0
    final = [] 
    t = 0
    for y in arr:
        t = y
        for x in range(n):
            temp = temp + (int(t)%10)
            t = int(t/10)
        t = 0    
        if temp == sum:
            final.append(y)
        temp = 0        
    print(final)
    print("Count  = {}".format(len(final)))
    final.clear()        

def getCount(n,sum):
    arr = [] 
    if n == 2:
        arr = range(11,100)
        processing(n,sum,arr)    
    elif n == 3:
        arr = range(100,1000)
        processing(n,sum,arr)    
    elif n == 4:
        arr = range(1000,10000)
        processing(n,sum,arr)    
    elif n == 5:
        arr = range(10000,100000)
        processing(n,sum,arr)        
    else: 
        print("Enter a valid digit number please")        
        

getCount(2,3)
getCount(3,3)
getCount(4,3)
getCount(5,3)