class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        limit  = int(num**0.5)
        total = 1
        for i in range(2,limit+1):
            if num % i == 0:
                total += i
                if i != (num // i):
                    total += ( num // i) 
                
        return total == num