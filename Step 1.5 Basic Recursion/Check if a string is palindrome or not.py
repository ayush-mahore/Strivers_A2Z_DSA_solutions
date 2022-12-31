#User function Template for python3
class Solution:
    def isPalindrome(self, s, i= 0):
        if s[i] != s[len(s)-i-1]:
            return 0
        if i >= len(s)//2:
            return 1
        return self.isPalindrome(s, i+1)
        
