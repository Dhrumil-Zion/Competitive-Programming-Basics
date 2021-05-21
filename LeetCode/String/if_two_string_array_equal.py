word1=["ab","c"]
word2=["a","bc"]

w1 = ''.join(word1)
w2 = ''.join(word2)
if w1 == w2:
    print(True)
print(False)

print("".join(word1)=="".join(word2))  ## memory usage is higer then above code