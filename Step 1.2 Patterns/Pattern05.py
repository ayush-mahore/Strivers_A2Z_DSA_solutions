# * * * * *
# * * * * 
# * * * 
# * *  
# * 

#User function Template for python3

class Solution:
    def printTriangle(self, N):
        for i in range(N): # 1 2 3 4
            for j in range(N-i): # 0 1 2 3 
                print("*", end= " ")
            print()
            
