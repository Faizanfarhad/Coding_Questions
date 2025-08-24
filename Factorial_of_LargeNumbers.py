#User function Template for python3

class Solution:
    def factorial(self, n):
        #code here
        ans = []
        if n == 0 or n == 1:
            ans.append(1)
            return ans
        Sum = 1
        for i in range(n,0,-1):
            Sum *= i
        for c in str(Sum):
            ans.append(int(c))
        return ans
