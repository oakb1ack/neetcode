class Solution:
    def jump(self, nums: List[int]) -> int:
        res = r = l = 0
        n = len(nums)
        farthest = 0

        while r < n-1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            print(r)
            res += 1

        return res