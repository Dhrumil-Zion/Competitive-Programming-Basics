(n, k) = map(int, input().split(' '))
ans = 0
for _ in range(n):
	x = int(input())
	if x % k == 0:
		ans += 1
print(ans)	