from math import log,exp
def getSum(a, b):
    # return sum([a,b])
    return int(log(exp(a)*exp(b)))
print(getSum(1,2))