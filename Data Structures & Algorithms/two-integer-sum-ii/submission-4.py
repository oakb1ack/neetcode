class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        l, r = 0, n - 1
        ans = [-1, -1]

        while l < r: 
            tot = numbers[l] + numbers[r]

            if tot > target:
                r -= 1
            elif tot < target: 
                l += 1
            elif tot == target:
                return [l + 1, r + 1]
        
        return ans