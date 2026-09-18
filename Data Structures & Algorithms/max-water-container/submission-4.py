class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        p1, p2 = 0, len(heights) - 1

        while p1 < p2:
            curMaxWater = min(heights[p1], heights[p2]) * (p2 - p1) 
            maxWater = max(curMaxWater, maxWater)

            if heights[p1] > heights[p2]:
                p2 -= 1
            else:
                p1 += 1

        return maxWater