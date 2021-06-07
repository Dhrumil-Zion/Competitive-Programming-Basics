def strStr(haystack, needle):
    if needle in haystack:
        return (haystack.index(needle))
    else:
        return -1 
print(strStr("hello","ll"))