# 1
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5


class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            for j in range(1,i+1):
                print(i, end = " ")
            print()