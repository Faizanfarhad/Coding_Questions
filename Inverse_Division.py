class Solution:
    def modDivide(a,b,M):
        try:
            res = (a * pow(b,-1,M)) % M
            return res
        except:
            return -1 
