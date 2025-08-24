# import math #Level :- Medium , PLatform :- GfG
class Solution:
    def isPrime(self, n : int) -> str:
        # code here
        ans = 'Yes'
        if n == 1 or n < 1:
            ans = 'No'
            return ans
        if n == 2:
            return ans
        for i in range(2,n):
            if n % i == 0:
                ans = 'No'
                return ans
                break
        return ans
