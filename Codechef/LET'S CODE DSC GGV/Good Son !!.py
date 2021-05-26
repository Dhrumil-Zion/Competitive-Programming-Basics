# https://www.codechef.com/LETS2021/problems/LETSC006/
def goodson(s):
    n = len(s)
    arr = [0]*(n+1)
    for i in range(n):
        if s[i] == '<':
            arr[i+1] = arr[i]+1

    for i in reversed(range(n)):
        if s[i] == '>':
            arr[i] = max(arr[i+1]+1, arr[i])
    return sum(arr)


if __name__ == '__main__':
    s = input()
    print(goodson(s))
