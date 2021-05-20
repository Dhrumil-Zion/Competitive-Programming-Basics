def flippingBits(n):
    binary = "{:032b}".format(n)
    z = [str(abs(1-int(x))) for x in binary]
    return int("".join(z),2)