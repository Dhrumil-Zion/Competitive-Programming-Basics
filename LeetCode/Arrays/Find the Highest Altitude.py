def largestAltitude(gain):
        su = 0
        m = 0
        for c in gain:
            su+=c
            if su>m:
                m=su
        return (m)
gain = [-5,1,5,0,-7]
print(largestAltitude(gain))