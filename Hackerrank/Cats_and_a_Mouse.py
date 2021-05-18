def catAndMouse(x, y, z):
    temp=0
    temp1=0
    temp = x-z if x>z else z-x
    temp1 = y-z if y>z else z-y
    if temp > temp1:
        return "Cat B"
    elif temp <temp1:
        return "Cat A"
    elif temp==temp1:
        return "Mouse C"