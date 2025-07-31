class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        Prime = [True] * (n)
        Prime[0],Prime[1] = False,False
        p = 2
        while ((p * p) < n):
            if Prime[p]:
                for i in range(p*p,n,p):
                    Prime[i] = False
            p += 1
        
        return sum(Prime) 
