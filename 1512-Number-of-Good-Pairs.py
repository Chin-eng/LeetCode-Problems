class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)

        def formula(n):
            return n * (n - 1) // 2

        for num in nums:
            hashmap[num] += 1
        
        ans  = 0

        for value in hashmap.values():
            pairs = formula(value)
            ans += pairs

        return ans

        