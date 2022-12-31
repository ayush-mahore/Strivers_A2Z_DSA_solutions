
# ABCDE
# ABCD
# ABC
# AB
# A


#User function Template for python3

class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            for j in range(ord("A"), ord("A")+(N-i+1)):
                print(chr(j), end = "")
                
            print()
