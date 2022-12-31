# 1 
# 0 1 
# 1 0 1
# 0 1 0 1 
# 1 0 1 0 1

#User function Template for python3

class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            for j in range(i):
                print((i+j)%2, end = " ")
            print()
            