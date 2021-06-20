def uniqueMorseRepresentations(words):
    mapper = {'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",
                    'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",
                    'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",
                    'q':"--.-",'r':".-.",'s':"...",'t':"-",
                    'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
    ans = ["".join(mapper[w] for w in wo) for wo in words]
    print(ans)
    return len(list(set(ans)))

print(uniqueMorseRepresentations(["gin", "zen", "gig", "dhrumil"]))