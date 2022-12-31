class Solution:
    def armstrongNumber (ob, n):
        numi, n_copy = 0, n
        while n_copy!= 0:
            k = n_copy%10
            numi += (k)**3
            n_copy = n_copy//10
        return "Yes" if numi==n else "No"