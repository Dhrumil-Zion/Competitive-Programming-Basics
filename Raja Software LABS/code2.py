def spt(st):
    f = st.split('.')
    temp = []
    for v in range(len(f)):
        if v%2!=0:
            temp.append(f[v][::-1])
        else:
            temp.append(f[v])
    print(".".join(temp))


st = "i.like.this.program.very.much"
spt(st)