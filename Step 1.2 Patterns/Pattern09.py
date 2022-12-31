#User function Template for python3
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 



class Solution:
    def printTriangle(self, N):
        for i in range(N):
        
            for j in range(N-i-1):
                print(" ", end = "")
            
            for j in range(i+1):
                print("*",end = " ")
            
            print()
            
        for i in range(N):
            
            
            for j in range(i):
                print(" ", end = "")
            
            
            for j in range(N-i):
                print("*", end = " ")
            
            print()
