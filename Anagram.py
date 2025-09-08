class Solution:
    def Anagram(self,s1,s2):
        if len(s1)!= len(s2):
            return False
        s1 = ''.join(sorted(s1))
        s2 = ''.join(sorted(s2))
        if s1 == s2:
            return True
        return False
        
