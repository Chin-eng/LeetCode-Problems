class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])

        hashmap = defaultdict(int)
        hashmap[0] = 1

        ans = 0
        for num in prefix:
            ans += hashmap[num-goal]
            hashmap[num] += 1

        return ans
        
        
        