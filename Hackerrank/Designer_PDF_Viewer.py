def designerPdfViewer(h, word):
    char = "a"
    z = []
    s = []
    abc = []
    i = ord(char[0])
    z.append(char)
    for _ in range(25):
        i += 1
        char = chr(i)
        z.append(char)
    for x in range(len(word)):
        j = word[x]
        k = z.index(j)
        abc.append(h[k])

    return (max(abc)*len(word))