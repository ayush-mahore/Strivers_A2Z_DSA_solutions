# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15

#User function Template for python3

class Solution:
    def printTriangle(self, N):
        sumi = 1
        for i in range(1, N+1):
            for j in range(i):
                print(sumi, end = " ")
                sumi += 1
            print()
