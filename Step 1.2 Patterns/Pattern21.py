# ****
# *  *
# *  *
# ****


class Solution:
    def printTriangle(self, N):
        print('*'*N)
        if(N>1):
            for i in range(1,N-1):
                print('*' + ' '*(N-2) + '*')
            print('*'*N)