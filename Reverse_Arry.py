######################################### For Numbers Only #########################################

def reverseNumber(s):
    st = 0 
    en = -1 
    for x in range(int(len(s)/2)):
        s[st],s[en] = s[en],s[st]
        st = st + 1
        en = en - 1
    print(s)     

######################################### For Strings Only #########################################

def reverseWord(s):
    j = -1
    k = ""
    for x in range(len(s)-1):
        k = k + s[j]
        j = j - 1
    k = k + s[-len(s)]
    print(k) 

def reverse(s): 
    str = "" 
    for i in s: 
        str = i + str
    print(str)

def reverseString(string): 
	string = "".join(reversed(string)) 
	print(string) 

def reverse_list(s):
    temp_list = list(s)
    temp_list.reverse()
    final = ''.join(temp_list)
    print(final)    

def reverse_recursion(s):
    if len(s) == 0:
        return s
    else:
        return reverse_recursion(s[1:]) + s[0]    

######################################### Generic for Both #########################################

def reverseList(A):
    print( A[::-1])



i = [1,2,3,4,5]
k = [6,7,8,9,10]
j = "Dhrumil"

reverseNumber(i)
reverseWord(j)	
reverseList(k)
reverseList(j) 
reverse(j)
reverseString(j)
reverse_list(j)
print(reverse_recursion(j))