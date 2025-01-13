class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])

        hashmap = defaultdict(int)
        hashmap[0] = 1

        ans = 0

        for num in prefix:
            if (num - k) in hashmap:
                ans += hashmap[num-k]   
            hashmap[num] += 1

        return ans

        