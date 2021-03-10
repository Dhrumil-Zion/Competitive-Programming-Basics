R = 3
C = 3

def prefixSum2D(a) :
	global C, R
	psa = [[0 for x in range(C)] 
			for y in range(R)] 
	psa[0][0] = a[0][0]

	for i in range(1, C) :
		psa[0][i] = (psa[0][i - 1] +
					a[0][i])
	for i in range(0, R) :
		psa[i][0] = (psa[i - 1][0] +
					a[i][0])

	for i in range(1, R) :
		for j in range(1, C) :

			psa[i][j] = (
                psa[i - 1][j] + psa[i][j - 1] - psa[i - 1][j - 1] + a[i][j]
            )

	for i in range(0, R) :
		for j in range(0, C) :
			print (psa[i][j], 
				end = " ")
		print ()

a = [
    [10,20,30],
    [5,10,20],
    [2,4,6]
]

prefixSum2D(a)
