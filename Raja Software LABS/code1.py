s = "rajasoftwarelabs"
f = s.lower()
arr = []   ## b,f,j,p,v
sum =0
for v in ['b','f','j','p','v']:
    if s.count(v)>0:
        sum+=s.count(v)
        arr.append(str(v+"="+str(s.count(v))))
print(",".join(arr)+",others="+str(len(s)-sum))