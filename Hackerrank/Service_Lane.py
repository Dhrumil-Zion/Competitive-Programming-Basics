def serviceLane(n, cases,width):
    return [min(width[x[0]:x[1]+1]) for x in cases]