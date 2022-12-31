# 1                 1
# 1 2             2 1
# 1 2 3         3 2 1
# 1 2 3 4     4 3 2 1
# 1 2 3 4 5 5 4 3 2 1

#User function Template for python3

class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            
            for j in range(1,i+1):
                print(j, end = " ")
            
            for j in range((N-i)*2):
                print(" ", end = " ")
            
            for j in range(i, 0, -1):
                print(j, end = " ")
            
            print()
