class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)

        l, r = 0, n -1

        while l < r: 
            while l < r and s[l].isalnum() == False:
                l += 1
            while r > l and s[r].isalnum() == False:
                r -= 1
            if l < r and s[r].lower() != s[l].lower():
                return False
            l, r = l + 1, r - 1
        
        return True