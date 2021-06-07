def isPalindrome(s):
    s =s.lower()
    st = "".join(c for c in s if c.isalnum())
    return st==st[::-1]
print(isPalindrome("askjdsak asidubsakdj sdkjsa dk`3221jb312 kj213k;213j 2kjb"))