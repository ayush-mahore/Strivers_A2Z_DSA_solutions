#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        
        arr = [1, 1]

        if n == 1:
            return [1]
        
        for i in range(2,n):
            arr.append(arr[i-2]+ arr[i-1])
        
        return arr
