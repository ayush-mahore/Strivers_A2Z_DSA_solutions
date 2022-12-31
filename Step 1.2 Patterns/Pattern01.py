#       * * * * *
#       * * * * *
#       * * * * *
#       * * * * *
#       * * * * *          

class Solution:
    def printSquare(self, n):
        for i in range(n):
            for j in range(n):
                print("*", end = " ")
            print()