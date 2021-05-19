digits = [1,2,3]
string_ints = [str(int) for int in digits]
s = "".join(string_ints)
c = int(s)+1
temp = [int(v) for v in str(c)]
print(temp)