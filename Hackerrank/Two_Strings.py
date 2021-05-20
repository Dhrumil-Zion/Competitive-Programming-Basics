def twoStrings(s1, s2):
    extra = list(set(s1))
    temp = list(set(s2))
    for item in extra:
        if item in temp:
            return "YES"
    return "NO"