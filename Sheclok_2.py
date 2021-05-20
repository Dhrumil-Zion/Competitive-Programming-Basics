import math
def squares(a, b):
    c  = int(math.sqrt(a))
    d = int(math.sqrt(b))
    print(c)
    print(d)
    su = d-c
    if c**2 == a:
        su +=1
    if d**2 == b:
        su+=1
    print(su)    

squares(3,9)    