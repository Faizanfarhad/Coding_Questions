import math
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums = sorted(nums)
        def istriangle(a,b,c):
            if (a + b )> c:
                return True
            return False
        def isareazero(a,b,c):
            s= (a + b + c) / 2
            area = math.sqrt(s*((s-a) * (s-b) * (s-c)))
            if area != 0 :
                return True
            return False

        n = len(nums) 
        if len(nums) == 3:
            if istriangle(nums[0],nums[1],nums[2]):
                if isareazero(nums[0],nums[1],nums[2]):
                    return sum(nums)
            return 0
        out = 0
        for i in  range(1,(n-2 + 1)):
            if istriangle(nums[i-1],nums[i],nums[i+1]):
                if isareazero(nums[i-1],nums[i],nums[i+1]):
                    curr_sum = nums[i-1] + nums[i] + nums[i+1]
                    out = max(out,curr_sum)
        return out 
