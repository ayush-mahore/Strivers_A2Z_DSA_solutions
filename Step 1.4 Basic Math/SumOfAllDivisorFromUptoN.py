class Solution:
    def sumOfDivisors(self, N):
        sumi = 0
        for i in range(1, N+1):
            sumi += (N//i)*i
        return sumi
