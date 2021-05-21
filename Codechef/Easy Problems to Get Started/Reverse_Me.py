# Problem Name: Reverse Me 
# Problem Code: REVMEE

N = int(input())
lst = list(map(int, input().split()))
lst.reverse()
print(*lst)