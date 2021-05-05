v =input()
nu = int(input())
an = []
n = len(v)
while nu!=0:
    j = 0
    i = 0
    d =input()
    m = len(d)
    while j < m and i < n:
        if d[j] == v[i]:
            j += 1
        i += 1
    if j == m:
        an.append("POSITIVE")
    else:
        an.append("NEGATIVE")
    nu-=1

print(*an,sep='\n')


# def isSubSequence(str1, str2):
# 	m = len(str1)
# 	n = len(str2)

# 	j = 0 # Index of str1
# 	i = 0 # Index of str2

# 	# Traverse both str1 and str2
# 	# Compare current character of str2 with
# 	# first unmatched character of str1
# 	# If matched, then move ahead in str1

# 	while j < m and i < n:
# 		if str1[j] == str2[i]:
# 			j += 1
# 		i += 1

# 	# If all characters of str1 matched,
# 	# then j is equal to m
# 	return j == m

# print ("Yes" if isSubSequence(str1, str2) else "No")

# # Contributed by Harshit Agrawal
