# 4 4 4 4 4 4 4
# 4 3 3 3 3 3 4
# 4 3 2 2 2 3 4
# 4 3 2 1 2 3 4
# 4 3 2 2 2 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4

class Solution:
    def printTriangle(self, N):
        for i in range(1-N, N):
            for j in range(1-N, N):
                if abs(i) > abs(j):
                    print(abs(i) + 1, end = " ")
                else:
                    print(abs(j) + 1, end = " ")
            print()