class Solution:
    def median(self, arr):
        n = len(arr)
        sorted_arr = sorted(arr)
        if n % 2 == 0:
            return (sorted_arr[n//2] + sorted_arr[(n//2) - 1]) // 2
        return sorted_arr[len(sorted_arr)//2]

    def mean(self, arr):
        arr_sorted = sorted(arr)
        i = 0
        Sum = 0
        while i < len(arr_sorted):
            Sum += arr_sorted[i]
            i += 1
        return Sum // len(arr)
