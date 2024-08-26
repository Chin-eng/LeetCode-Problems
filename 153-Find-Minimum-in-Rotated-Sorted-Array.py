class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) -1

        minValue = float('inf')

        while left <= right:
            mid = (left + right) // 2

            minValue = min(minValue, nums[mid])

            if nums[mid] >= nums[left]:
                minValue = min(minValue, nums[left])
                left = mid + 1
            else:
                minValue = min(minValue, nums[right])
                right = mid - 1
        
        return minValue

