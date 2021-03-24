def weightedUniformStrings(s, queries):
    li = ["","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
        "p","q","r","s","t","u","v","w","x","y","z"]
    z = []
    temp = 0
    s = list(s)
    for x in range(len(s)):
        k=0
        r = x+1
        while k!=s.count(s[x]):
            temp =temp+r
            z.append(temp) 
            k+=1
        temp=0    
    print(z)      

s = "aabbbb"
qu = [5,9,7,8,12,5]
weightedUniformStrings(s,qu)