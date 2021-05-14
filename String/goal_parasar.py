command = "G()()()()(al)"
st = ""
for v in range(len(command)):
    if command[v]=='G':
        st+="G"
    elif command[v:v+2]=='()':
        st+="o"
    elif command[v:v+4]=="(al)":
        st+="al"
print(st)