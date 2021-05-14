def funcName(s):
    arr = []
    for v in s:
        if s.count(v)>0:
            t = v+str(s.count(v))
            if t in arr:
                continue
            arr.append(t)
        else:
            arr.append(v)
    compress_s ="".join(arr)
    if len(compress_s)>=len(s):
        return s
    else:
        return compress_s
    
s = "abcddddsdsda"
print(funcName(s))