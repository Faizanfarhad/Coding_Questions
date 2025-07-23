class Solution:
    def __init__(self):
        super().__init__()
    def printDivisor(self,n):
        divisors = []
        i = 1
        while i < n+1:
            if n % i == 0:
                divisors.append(i)
            i = i+1
        return divisors


