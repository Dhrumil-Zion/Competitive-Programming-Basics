# https://www.codechef.com/LETS2021/problems/LETSC005/
def largestground(r, c, arr):
    t = 0
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 1:
                arr[i][j] = 0
            else:
                arr[i][j] = 1
                t = 1
    for i in range(1, r):
        for j in range(1, c):
            if arr[i][j] != 0:
                t = max(t, 1)
                arr[i][j] = arr[i][j] + \
                    min(arr[i-1][j], arr[i-1][j-1], arr[i][j-1])
                t = max(t, arr[i][j])
    return t*t


if __name__ == '__main__':
    r, c = map(int, input().split())
    arr = [[0]*c for _ in range(r)]
    for i in range(r):
        arr[i] = list(map(int, input().split()))
    print(largestground(r, c, arr))
