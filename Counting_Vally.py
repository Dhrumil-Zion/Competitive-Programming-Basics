def countingValleys(steps, path):
    sealevel = 0
    count = 0
    for x in range(steps):
        if path[x]=='D' and sealevel ==0:
            sealevel = sealevel - 1
            count +=1
        elif path[x] == 'D':
            sealevel = sealevel - 1
        elif path[x] == 'U':
            sealevel = sealevel + 1    
    return count

a = "UDDDUDUU"

countingValleys(len(a),a)
