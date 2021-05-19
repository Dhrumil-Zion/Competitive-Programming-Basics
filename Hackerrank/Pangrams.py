def pangrams(s):      
    a = list(set(s.lower()))
    if " " in a:
        a.remove(" ")    
    if len(a)==26:
        return "pangram"
    else:
        return "not pangram"