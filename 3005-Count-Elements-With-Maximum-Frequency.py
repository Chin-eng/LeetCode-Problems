class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1

        maxVal = float("-inf")
        maxValues = set()

        for key in hashmap:
            maxVal = max(maxVal, hashmap[key])
        
        for key in hashmap:
            if maxVal == hashmap[key]:
                maxValues.add(key)
        
        ans = 0

        for key in hashmap:
            if key in maxValues:
                ans += hashmap[key]     
        
        return ans

        