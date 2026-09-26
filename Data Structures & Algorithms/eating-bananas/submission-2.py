class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = max(piles)

        while l <= r:
            guess = (l + r) //2
            curHours = 0
            for i in piles:
                curHours += math.ceil(float(i) / guess)
            if curHours <= h: 
                ans = min(ans, guess)
                r = guess -1
            else:
                l = guess + 1
        
        return ans 