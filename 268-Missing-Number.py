class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        seen1 = set()

        for i in range(n):
            seen1.add(i)

        seen2 = set()

        for num in nums:
            seen2.add(num)

        for num in seen1:
            if num not in seen2:
                return num
        
        return -1

        