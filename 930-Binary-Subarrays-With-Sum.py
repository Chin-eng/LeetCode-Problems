class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def helper(goal):
            if goal < 0: return 0
            left2, ans2, curr2 = 0, 0, 0
            for right in range(len(nums)):
                curr2 += nums[right]
                while left2 <= right and curr2 > (goal):
                    curr2 -= nums[left2]
                    left2 += 1
                ans2 += right - left2 + 1
            return ans2
        
        return helper(goal) - helper(goal -1)
        
        
        
        