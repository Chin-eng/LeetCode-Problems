class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        prefix = [nums[0] % 2]

        for i in range(1, len(nums)):
            prefix.append((nums[i] % 2) + prefix[-1])

        hashmap = defaultdict(int)

        hashmap[0] = 1
        ans = 0
        
        for element in prefix:
            ans += hashmap[element-k]
            hashmap[element] += 1
        
        return ans
        