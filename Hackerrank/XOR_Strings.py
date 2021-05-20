def strings_xor(s, t):
    return "".join('0' if s[i] == t[i] else '1' for i in range(len(s)))