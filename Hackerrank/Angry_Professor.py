def angryProfessor(k, a):
    c = 0
    for x in a:
        if x<=0:
            c+=1
        if c==k:
            return "NO"
    return "YES"     