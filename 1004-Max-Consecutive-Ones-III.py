class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        if len(nums) == k: return len(nums)

        left = 0
        n, ans = 0, float("-inf")
        for right in range(len(nums)):
            if nums[right] == 0:
                n += 1
            while n > k:
                if nums[left] == 0:
                    n -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans if ans != float("-inf") else 0

        # max = 5

        