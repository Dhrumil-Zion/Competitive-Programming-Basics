import string

alphabet = string.ascii_uppercase

def convertToTitle(n):
    result = ""
    while n > 0:
        n -= 1
        n, i = divmod(n, 26)
        result += alphabet[i]
    return result[::-1]

print(convertToTitle(701))