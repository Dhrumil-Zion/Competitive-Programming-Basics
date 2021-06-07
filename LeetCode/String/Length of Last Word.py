def lengthOfLastWord(s):
    return len(s.strip(" ").split(" ")[-1]) 

print(lengthOfLastWord("heelo world"))