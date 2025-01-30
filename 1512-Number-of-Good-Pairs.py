class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        ans = 0
        for num in nums:
            if num in hashmap:
                ans += hashmap[num]
            hashmap[num] += 1

        return ans
        