# 1 2 3 4 5
# 1 2 3 4
# 1 2 3 
# 1 2  
# 1 

#User function Template for python3

class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            for j in range(1,N-i+2):
                print(j, end = " ")
            print()
