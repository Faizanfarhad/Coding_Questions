class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient = int(dividend/divisor)
        start_32 = -2**31
        end_32 = (2**31) - 1 
        if quotient < start_32:
            return start_32 
        if quotient > end_32:
            return  end_32
        return quotient