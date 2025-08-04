class Solution:
    def nCr(self,n,r):
        if r > n:
            return 0
        if r == 0:
            return 1

        def factorial(n):
            Sum = 1
            for i in range(n,0,-1):
                Sum *= i
            return Sum
        return factorial(n) // (factorial(n - r) * factorial(r))
    

