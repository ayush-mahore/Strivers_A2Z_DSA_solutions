
class Solution:
    def generate(self, numRows: int):
        lst = [[1]]
        for i in range(1, numRows):
            new = [1]
            for j in range(len(lst[-1])-1):
                new.append(lst[-1][j] + lst[-1][j+1])
            new.append(1)
            lst.append(new)
        
        return lst