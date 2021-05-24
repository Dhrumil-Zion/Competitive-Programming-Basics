words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
def findAndReplacePattern(words, pattern):
        pattern = word2Num(pattern)
        print([word for word in words if word2Num(word) == pattern])
        
def word2Num(word):
    ch2Digit = {}
    digits = []
    for ch in word:
        if ch not in ch2Digit: ch2Digit[ch] = len(ch2Digit)
        digits.append(ch2Digit[ch])
    return digits
findAndReplacePattern(words,pattern)