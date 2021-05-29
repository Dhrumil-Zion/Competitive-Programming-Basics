c = 0
def check(s):
    global c
    if s.count('A')<2:
        if s.count('L') < 3:
            c+=1
        elif s.count('L') > 2 and 'LLL' not in s:
            c+=1

def printAllKLength(set, k):
	n = len(set)
	printAllKLengthRec(set, "", n, k)

def printAllKLengthRec(set, prefix, n, k):
    if (k == 0) :
        check(prefix)
        # print(prefix)
        return
    for i in range(n):
        newPrefix = prefix + set[i]
        printAllKLengthRec(set, newPrefix, n, k - 1)
	
set1 = ['A', 'L','P']
k = 10101
printAllKLength(set1, k)
print(c)