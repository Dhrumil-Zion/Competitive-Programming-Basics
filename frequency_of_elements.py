a = [1,2,3,1,3,5,6,1,2,5,3,7,8,4,2,7,9,4,5,2,1,5,2,3,7,8,4]
x = set(a)
for y in x:
    print("{} - {} times".format(y,a.count(y)))

"""
input : a = [1,1,3,4,4]
ouput : 2 0 1 2

Explain : 2 for 1 , 0 for 2 , 1 for 3 , 2 for 4        
"""


def frequencycount(A,N):
        a = []
        for x in range(1,N + 1):
            a.append(A.count(x))
        for y in a:
            print(y,end=" ")

arr =[2,3,2,3,5]
frequencycount(arr,5)