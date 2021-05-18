def countingValleys(steps, path):
    sealevel = 0
    count = 0
    for x in range(steps):
        if path[x]=='D' and sealevel ==0:
            sealevel -= 1
            count +=1
        elif path[x] == 'D':
            sealevel -= 1
        elif path[x] == 'U':
            sealevel += 1
    return count