#    A
#   ABA
#  ABCBA
# ABCDCBA

#User function Template for python3

class Solution:
    def printTriangle(self, N):
        for i in range(1, N+1):
            
            for j in range(N-i):
                print(" ", end = "")
                
            for j in range(ord("A"), ord("A")+i):
                print(chr(j), end = "")
            
            for j in range(ord("A")+i-2, ord("A")-1, -1):
                print(chr(j), end = "")
            
            print()
