def sum(i):
    sum = 0
    for _ in range(len(str(i))):
        sum += i % 10
        i = int(i /10)
    print(sum)    

def getSum(n):
    sum = sum(int(i) for i in n)
    print(sum)

def sumDigits(no):
	return 0 if no == 0 else int(no % 10) + sumDigits(int(no/10))

print(sumDigits(128376237621))
sum(128376237621)
getSum("128376237621")


