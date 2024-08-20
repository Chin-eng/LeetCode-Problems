class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        minVal = float('inf')
       
        while left <= right:
            mid = (left + right) // 2

            minVal = min(minVal, nums[mid])
            
            if nums[left] < nums[mid]:
                minVal = min(minVal, nums[left])
                left = mid + 1
            else:
                minVal = min(minVal, nums[right])
                right = mid - 1
        
        return minVal

        
        