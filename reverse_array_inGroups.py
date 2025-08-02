class Solution:
    def reverseInGroups(self, arr, k):
        n = len(arr)
        if k >= n:
            arr.reverse()
            return arr
        i = 0
        while i < n:
            l = i
            r = min(i + k, n) - 1
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            i += k
        return arr
