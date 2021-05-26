# https://www.codechef.com/LETS2021/problems/LETSC004/
def maximumprofit(arr, n):
    arr.sort(reverse=True)
    count = 0
    m = 0
    for i in range(n):
        count = (i+1)*arr[i]
        m = max(m, count)
    return m


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(maximumprofit(arr, n))
