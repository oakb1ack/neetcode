class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s) 
        s = s.lower()

        p1 = 0
        p2 = n - 1

        while p1 < p2: 
            while p1 < n and s[p1].isalnum() != True:
                p1 += 1
            while p2 > 0 and s[p2].isalnum() != True:
                p2 -= 1
            
            if p1 < p2 and s[p1] != s[p2]:
                return False
            
            p2 -= 1
            p1 += 1
            
        return True


