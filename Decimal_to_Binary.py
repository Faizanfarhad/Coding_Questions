# Solved on GeeksForGeeks DSA Skillup course
class Solution:
    def dectoBin(self,n):
        bin_lst = []
        while n > 0:
            remainder = n % 2 
            bin_lst.append(str(remainder))
            n //=2
        
        return "".join(bin_lst[::-1])