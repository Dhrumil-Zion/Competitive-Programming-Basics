import math
def checkPerfectNumber(num):
    divisorSum = 1
    if num <= 4:
        return False
    for x in range(2,math.ceil(math.sqrt(num))): 
        if num % x == 0:
            divisorSum += x + (num//x) 
    if (x+1)**2 == num:
        divisorSum += x
    return divisorSum == num

print(checkPerfectNumber(14213))