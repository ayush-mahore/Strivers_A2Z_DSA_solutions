

class Solution:
    def evenlyDivides (self, N):
        count = 0
        n = N
        while(n//10) != 0:
            k = n%10
            if k!= 0 and N%k == 0:
                count += 1
            n = n//10
        
        if N%n == 0:
            count += 1
        return count


