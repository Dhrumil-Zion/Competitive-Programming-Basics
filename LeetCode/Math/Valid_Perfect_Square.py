def isPerfectSquare(num):
    square = int(num**(1/2))
    return square**2 == num

print(isPerfectSquare(12382743827))