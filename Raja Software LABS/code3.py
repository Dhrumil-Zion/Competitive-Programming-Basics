import math
def non_prime_sum(arr):
    sum = 0
    for num in arr:
        if num > 1:
            for i in range(2, int(math.sqrt(num))+1):
                if (num % i) == 0:
                    sum+=num
                    break                                                             
        else:                                
            sum+=num
    print(sum)

arr = [1,14,5,7]
non_prime_sum(arr)