#     *
#    ***  
#   *****
#  *******
# *********

#User function Template for python3

class Solution:
    def printTriangle(self, N):
        for i in range(N): #1
            
            for j in range(N-i-1): #3  0 1 2
                print(" ", end = "")
            
            for j in range((2*i)+1): #0 1 2
                print("*", end = "")
                
            for j in range(N-i-1): #3  0 1 2
                print(" ", end = "")
            
            
            print()
