n = str(1234545)
le =  len(n)
ans = ""
if le%2==0:
    ans = n[:int((le/2))-1] + n[int((le/2))+1:]
if le%2!=0:
    ans = n[:int((le/2))]+n[int((le/2))+1:]
print(ans)