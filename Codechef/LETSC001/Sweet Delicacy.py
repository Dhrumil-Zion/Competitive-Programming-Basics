# https://www.codechef.com/LETS2021/problems/LETSC002
def sweetdelicacy(n):
    c = 0
    while n != 1:
        if n % 2:
            n = n-1
            c += 1
        else:
            n = n//2
    return c+1


if __name__ == '__main__':
    n = int(input())
    print(sweetdelicacy(n))
