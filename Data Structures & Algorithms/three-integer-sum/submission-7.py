class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(len(nums)):
            p1 = i+1 
            p2 = len(nums) - 1 

            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while p1 < p2:
                value = nums[i] + nums[p1] + nums[p2]
                if value == 0:
                    ans.append([nums[i], nums[p1], nums[p2]])
                    p2-= 1 
                    p1 += 1
                    while p1 < p2 and nums[p1] == nums[p1-1]:
                        p1+= 1
                elif value > 0:
                    p2 -= 1
                else:
                    p1 += 1
                    
        return ans