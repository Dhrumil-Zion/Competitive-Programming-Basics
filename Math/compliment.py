n=10
i=bin(n).replace("0b","")
cmp_bin = ""
for v in i:
    if v=='1':
        cmp_bin+='0'
    elif v=='0':
        cmp_bin+='1'
print(int(cmp_bin,2))