T = int(input())
def factorial(n):
    if n in [1, 0]:
        return 1
    else: 
        return n * factorial(n-1)
while T!=0:
    num = int(input())
    fact = factorial(num)
    print(fact)
    T-=1