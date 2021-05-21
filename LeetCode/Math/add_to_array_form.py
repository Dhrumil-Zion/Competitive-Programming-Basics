num = [1,2,2]
k=3
string_ints = [str(int) for int in num]
s = "".join(string_ints)
c = int(s)+k
temp = [int(v) for v in str(c)]
print(temp)