# Complete the caesarCipher function below.
def caesarCipher(s, k):
    k = k% 26
    l = list(s)
    e = []
    for item in l:
        z = ord(item)
        if (z >= 97 and z <= 122) and (z + k) > 122:
            e.append(chr(96 + (z+k-122)))
        elif z >= 97 and z <= 122 or z >= 65 and z <= 90 and z + k <= 90:
            e.append(chr(z+k))
        elif z >= 65 and z <= 90:
            e.append(chr(64 + (z+k-90)))
        else:
            e.append(item)
    print("".join(e))


s ="middle-Outz"
k=3 
caesarCipher(s,k)   
