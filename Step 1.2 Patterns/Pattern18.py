# E
# E D
# E D C
# E D C B
# E D C B A

#User function Template for python3

class Solution:
    def printTriangle(self, N):
        for i in range(1, N+1):
            for j in range(ord("A")+N-1, (ord("A")+N-1)-i, -1):
                print(chr(j), end = " ")
            print()
