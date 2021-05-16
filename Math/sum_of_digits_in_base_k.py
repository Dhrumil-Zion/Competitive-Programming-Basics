import numpy as np
n = 34
k = 6
print(sum(int(i) for i in str(np.base_repr(n, base=6))))

## some what faster 

out = 0
while n != 0:
    q = n // k
    r = n % k
    out += r
    n = q
print(out)