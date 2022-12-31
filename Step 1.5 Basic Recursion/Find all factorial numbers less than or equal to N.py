#User function Template for python3

class Solution:
    def factorialNumbers(self, N):
        fac = 1
        arr = [1]
        for i in range(2,N+1):
            fac *= i
            if fac >= N+1:
                return arr
            arr.append(fac)
        return arr
        