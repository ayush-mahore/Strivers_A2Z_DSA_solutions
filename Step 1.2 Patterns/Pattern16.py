# A
# BB
# CCC
# DDDD
# EEEEE

#User function Template for python3

class Solution:
    def printTriangle(self, N):
        sumi = ord("A")
        for i in range(N):
            for j in range(i+1):
                print(chr(sumi), end = "")
            sumi += 1
            print()
