class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return
        
        k = k%n

        if k == 0:
            return 
        
        arr = nums[-k:]
        i = 0
        while i < (n- k):
            arr.append(nums[i])
            i += 1
        nums[:] = arr[:]
        
