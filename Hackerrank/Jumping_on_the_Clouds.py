def jumpingOnClouds(c):
    x=0
    count=0
    while x!=len(c)-1:
        if x == len(c)-2:
            count +=1
            break
        if c[x+1] == 0 and c[x+2]==0:
            x += 2
            count+=1
        elif c[x+1]==0 and c[x+2]==1:
            x += 1
            count+=1
        elif c[x+1]==1 and c[x+2]==0:
            x += 2
            count+=1
    return count  