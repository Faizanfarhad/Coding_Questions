class Solution:
    def __init__(self):
        super().__init__()
    def lcm(self,a,b):
        def gcd(a,b):
            return a if b == 0 else gcd(b,a % b)

        return (a // gcd(a,b)) * b

"""
Example for a = 12 and b = 18:-
 gcd of a and b = 6 
    because 12 % 18 = 6
 lcm = 12 // 6 * 18 
     = 2 * 18 
    = 36
"""
