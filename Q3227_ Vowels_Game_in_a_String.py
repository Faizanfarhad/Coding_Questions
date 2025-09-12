class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vow = ['a','e','i','o','u','A','E','I','O','U']
        for i in s:
            if i in vow:
                return True
        return False
