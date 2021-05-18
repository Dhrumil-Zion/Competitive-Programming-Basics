import math
def viralAdvertising(n):
    like = 0
    z=5
    cu = 0
    while n!=0:
        like = math.floor(z/2)
        cu += like
        z = like *3
        n-=1
    return cu