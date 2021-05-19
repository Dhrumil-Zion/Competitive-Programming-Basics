def marsExploration(s):
    l =['S','O','S']
    c=0
    k = 0
    string = [str(x) for x in s]
    le = len(string)
    while k!=le:
        i = 0
        while i!=3:
            if l[i]!=string[k]:
                c+=1
            i+=1
            k+=1
    return c