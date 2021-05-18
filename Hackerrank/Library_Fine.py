def libraryFine(d1, m1, y1, d2, m2, y2):
    if m1==m2 and y1==y2 and d1==d2:
        return 0
    if m1==m2 and y1==y2:
        if d1<d2:
            return 0
        elif d1>d2:
            return (d1-d2) *15
    if  y1<y2:
        return 0
    elif y1>y2:
        return 10000
    if y1==y2 and m1<m2:
        return 0
    if y1<y2 and m1<m2:
        if d1<d2:
            return 0
        elif d1>d2:
            return (d1-d2) *15
    if m1>m2 and y1==y2:
        return (m1-m2)*500 