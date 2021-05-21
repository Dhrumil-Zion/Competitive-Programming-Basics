from functools import reduce

i=4421
su=0
mul=1
for v in str(i):
    mul*=int(v)
    su+=int(v)
print(mul-su)

n = [int(it) for it in str(i)]
pro = reduce((lambda x,y: x*y), n)
summ = reduce((lambda x,y: x+y), n)
print(pro - summ)