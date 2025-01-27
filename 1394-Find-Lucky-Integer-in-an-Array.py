class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = defaultdict(int)
        
        for num in arr:
            hashmap[num] += 1
        
        maxVal = float("-inf")

        for key in hashmap:
            if key == hashmap[key]:
                maxVal = max(maxVal, key)

        return maxVal if maxVal != float("-inf") else -1

        