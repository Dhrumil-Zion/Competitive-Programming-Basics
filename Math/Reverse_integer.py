import math
x = 120


########################## Optimized one by @LebronZheng

res = 0
sym = 1
# neg. cases
if x < 0:
    # symbol to -1
    sym = -1
    # value to positive
    x *= -1

while x:
    # find remainder
    rem = x % 10
    # add up to result
    res = res * 10 + rem
    # check former digit
    x = int(x/10)

# return result
if res >= pow(2, 31):
    print(0)
else:
    print(res * sym)



########################## more readable one 
range_32 = range(-2**31, 2**31-1)
if x not in range_32:
    final = 0
elif x < 0:
    final = -1 * int(str(x)[::-1][:-1])
else:
    final = int(str(x)[::-1])
print(final if final in range_32 else 0)


########################## first attempt     

mini_limit = -int(math.pow(2,31))
max_limit = int(math.pow(2,31))-1
num = -int(str(abs(x))[::-1]) if x <0 else int(str(x)[::-1])
if num < mini_limit or num > max_limit:
    print(0)
else:
    print(num)