import math
num =8
if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
    print (num)