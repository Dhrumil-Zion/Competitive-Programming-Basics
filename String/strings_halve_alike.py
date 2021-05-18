st = "AbCdEfGh"
a = st[:int(len(st)/2)].lower()
b = st[int(len(st)/2):].lower()
count_a = 0
count_b = 0
for a_,b_ in zip(a,b):
    if a_ in ['a','e','i','o','u']:
        count_a+=1
    if b_ in ['a','e','i','o','u']:
        count_b+=1
if count_a==count_b:
    print("yes")
else:
    print("no")