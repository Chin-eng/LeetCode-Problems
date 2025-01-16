class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        hashmap = defaultdict(int)

        ans = -1

        for num in nums:
            hashmap[num] += 1

        for key in hashmap:
            if hashmap[key] == 1:
                ans = max(ans, key)
        
        return ans
        