class Solution:
    def is_palindrome(self, X):
        if X < 10:
            return "Yes"
        numi = 0
        cop = X
        while X//10 != 0:
            numi *= 10
            k = X%10
            numi += k
            X = X//10
            if X < 10:
                numi *= 10
                numi += X
        return "Yes" if numi==cop else "No"