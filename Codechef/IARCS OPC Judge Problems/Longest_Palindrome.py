class Solution(object):
    def __init__(self):
        self.longPali = ""
    def checkPalindrome(self, s, left, right):
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -=1
            right +=1
        substr = s[left +1 : right]
        if len(substr) > len(self.longPali):
            self.longPali = substr
    def longestPalindrome(self, s):
        if len(s)==0:
            return ""
        for i in range(len(s)):
            self.checkPalindrome(s, i, i)
            self.checkPalindrome(s, i, i +1)
        return self.longPali

obj = Solution()
n = int(input())
string = input()
final_str = obj.longestPalindrome(string)
print(len(final_str))
print(final_str)


# def subString(s, n):
#     palindrom=[]
#     size =[]
#     for i in range(n):
#         for li in range(i+1,n+1):
#             st = s[i: li]
#             if st==st[::-1]:
#                 palindrom.append(st)
#                 size.append(len(st))
#     print(max(size))
#     print(palindrom[size.index(max(size))])

    
# s = "amma"
# subString(s,len(s))
