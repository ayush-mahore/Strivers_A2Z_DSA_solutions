#User function Template for python3

class Solution:
    def printGfg(self, n):
        if n > 0:
            print("GFG", end = " ")
            self.printGfg(n-1)
        
    
