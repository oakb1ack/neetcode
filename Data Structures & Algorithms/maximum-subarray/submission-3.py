class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        curTotal = nums[0]
        
        for i in range(1, len(nums)):
            curTotal = max(curTotal + nums[i], nums[i])
            print(curTotal)
            ans = max(curTotal, ans)

        return max(curTotal, ans)
