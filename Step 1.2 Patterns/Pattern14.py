# A
# AB
# ABC
# ABCD
# ABCDE


#User function Template for python3

class Solution:
    def printTriangle(self, N):
        for i in range(1, N+1):
            for j in range(ord("A"), ord("A")+i):
                print(chr(j), end = "")
            print()
