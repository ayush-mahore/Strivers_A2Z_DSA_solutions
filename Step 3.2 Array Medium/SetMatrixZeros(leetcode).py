

class Solution:


# ------------------- Brute Force ---------------------------------- #   
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    tempi = i
                    while tempi > 0:
                        if matrix[tempi-1][j] != 0:
                            matrix[tempi-1][j] = -1            
                        tempi -= 1
                    while tempi < n-1:
                        if matrix[tempi+1][j] != 0:
                            matrix[tempi+1][j] = -1
                        tempi += 1
                    while j > 0:
                        if matrix[i][j-1] != 0:
                            matrix[i][j-1] = -1
                        j -= 1
                    while j < m-1:
                        if matrix[i][j+1] != 0:
                            matrix[i][j+1] = -1
                        j += 1
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0



# --------------------------- Method 2 ------------------------------------------ #

    def setZeroes2(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        col, row = [None]*m, [None]*n

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0
        
        for i in range(n):
            for j in range(m):
                if row[i] == 0 or col[j] == 0:
                    matrix[i][j] = 0


# --------------------------------- Method 3 ---------------------------------- #

    def setZeroes3(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        col = True
        for i in range(n):
            if matrix[i][0] == 0: col = False
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        
        for i in range(n-1,-1,-1):
            for j in range(m-1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col is False:
                matrix[i][0] = 0