def camelcase(s):
    lis = [x for x in range(65,91)]
    return 1 + sum(ord(s[x]) in lis for x in range(len(s))) 