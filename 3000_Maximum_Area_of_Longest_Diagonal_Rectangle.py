from operator import mul
import math 
class Solution:
    def areaOfMaxDiagonal(self, mat: List[List[int]]) -> int:
        out_arr =[]
        i = 0
        j = 1

        while i < len(mat):
            landw_square = pow(mat[i][j],2) + pow(mat[i][j-1],2)
            diagonal = math.sqrt(landw_square)
            out_arr.append([diagonal,mul(mat[i][j],mat[i][j-1])])
            i += 1
        out = max(out_arr)
        return out[1] 
