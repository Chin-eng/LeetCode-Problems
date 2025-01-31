class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        left1, ans1, curr1 = 0, 0, 0
        for right in range(len(nums)):
            curr1 += nums[right]
            while curr1 > goal:
                curr1 -= nums[left1]
                left1 += 1
            ans1 += right - left1 + 1


        left2, ans2, curr2 = 0, 0, 0
        for right in range(len(nums)):
            curr2 += nums[right]
            while left2 <= right and curr2 > (goal - 1):
                curr2 -= nums[left2]
                left2 += 1
            ans2 += right - left2 + 1
        
        return ans1 - ans2
        
        
        
        