#User function Template for python3

class Solution:
    def lcmAndGcd(self, A , B):
        X = A
        Y = B
        while Y!= 0:
            X,Y = Y, X%Y
        if Y == 0:
            return int((A*B)/X),X
