sentence = "abcdefghijklmnopqrstuvwxyz"
print(True if len(set(sentence))==26 else False)  ## optimized in terms of memory usage

print( len(set(sentence))==26)