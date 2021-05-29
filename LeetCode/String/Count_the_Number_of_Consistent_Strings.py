allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]


## oneliner solution 

print(len([1 for word in words if set(word).issubset(allowed)]))


## somewhat slower than above one
count = sum(
    set(allowed).intersection(set(word)) == set(word) for word in words
)
print(count)
