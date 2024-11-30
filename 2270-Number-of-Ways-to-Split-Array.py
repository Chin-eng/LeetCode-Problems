class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        n = len(nums) - 1
        splits = len(nums) - 1
        ans = 0



        for i in range(splits):
            if prefix[i] >= prefix[n] - prefix[i]:
                ans += 1
        return ans



        