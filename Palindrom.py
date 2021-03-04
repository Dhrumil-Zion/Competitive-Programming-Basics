def isPalindrome(s):                #### Optimized way ####
	return s == s[::-1]

def isPalindrome_third(s):           #### Optimized way ####
	rev = ''.join(reversed(s))
	if (s == rev):
		return True
	return False

def isPalindrom_fifth(s):        #### for numbers only ####
    temp=s
    rev=0
    while(s>0):
        dig=s%10
        rev=rev*10+dig
        s=s//10
    if(temp==rev):
        print("The number is palindrome!")
    else:
        print("Not a palindrome!")        

def isPalindrom_one(i):                 #### Un-Optimized way Strings only####
    y = i 
    z = [x for x in i]
    a = [x for x in y]
    a.reverse()
    if z == a:
        print("Palindrom")
    else:
        print("Not")  

def isPalindrome_second(str):               #### Un-Optimized way ####
	for i in range(0, int(len(str)/2)): 
		if str[i] != str[len(str)-i-1]:
			return False
	return True

def isPalindrom_fourth(s):             #### Un-Optimized way Strings only ####
    w = ""
    for i in s:
        w = i + w
    if (s == w):
        print("Yes")
    else:
        print("No")


s = "malayalam"

isPalindrom_one(s)
ans = isPalindrome(s)
answer = isPalindrome_second(s)
anss = isPalindrome_third(s)
isPalindrom_fourth(s)
isPalindrom_fifth(121)

if anss:
	print("Yes")
else:
	print("No")
if answer:
	print("Yes")
else:
	print("No")
if ans:
	print("Yes")
else:
	print("No")
