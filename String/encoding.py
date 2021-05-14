s="a1c1e1"
st = []
ch=""
for c in s:
    if c.isalpha():
        st.append(c)
        ch=c
    else:
        new =int(ord(ch))+int(c)
        st.append(chr(new))
    
print(st)