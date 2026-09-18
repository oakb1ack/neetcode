class Solution:
    def isPalindrome(self, s): 
        n = len(s)
        s = s.lower()

        p1 = 0
        p2 = n - 1

        while p1 < p2:
            while p1 < p2 and s[p1].isalnum() == False:
                p1 += 1
            while p1 < p2 and s[p2].isalnum() == False:
                p2 -= 1 
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True


