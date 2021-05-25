import itertools

def findsubsets(s, n):
	return list(itertools.combinations(s, n))

s = {1, 2, 3,4,5,6}
n = 2

print(findsubsets(s, n))