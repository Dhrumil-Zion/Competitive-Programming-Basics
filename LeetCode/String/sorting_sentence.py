s = "is2 sentence4 This1 a3"
temp = s.split()
f = [""]*len(temp)
for t in temp:
    f[int(t[-1])-1]=t[:-1]
print(" ".join(f))