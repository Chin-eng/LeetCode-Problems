class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        frequency = defaultdict(int)

        left, ans = 0, 0

        for right in range(len(nums)):
            num = nums[right]
            frequency[num] += 1
            while frequency[num] > k:
                frequency[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans

            

        