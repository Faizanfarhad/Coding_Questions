class Solution:
    def __init__(self):
        super().__init__()
    def FloorandCeil(self,a,b):
        out = []
        floor = a // b
        ceil = -(-a//b)
        out.append(floor)
        out.append(ceil)
        return out
    
