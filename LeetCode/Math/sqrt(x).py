def mySqrt(x):
    if x==0 or x==1: return x
    if x==2 or x==3: return 1
    def square(val):
        return val*val

    l=2
    r=x//2+1
    while l<r:
        mid = l+(r-l)//2
        if square(mid)<=x:
            l = mid+1
        elif square(mid)>x:
            r = mid
    return l-1

print(mySqrt(1238398293))

# easy way 
print(21313**0.5)