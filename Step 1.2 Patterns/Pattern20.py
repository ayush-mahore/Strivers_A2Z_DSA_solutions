# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *


#User function Template for python3

class Solution:
    def printTriangle(self, N):
        for i in range(N-1):
            
            for j in range(i+1):
                print("*", end = "")
            
            for j in range(2*(N-i-1)):
                print(" ", end = "")
            
            for j in range(i+1):
                print("*", end = "")
                
            print()
        
        for i in range(N):
            
            for j in range(N-i):
                print("*", end = "")
            
            for j in range(2*(i)):
                print(" ", end = "")
                
            for j in range(N-i):
                print("*", end = "")
                
            print()