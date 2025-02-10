class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        hashmap = defaultdict(int)

        def getMax(hashmap):
            maxVal = float('-inf')
            for value in hashmap.values():
                maxVal = max(maxVal, value)
            return maxVal

        
        left , ans = 0, float('-inf')
        for right in range(len(s)):
            hashmap[s[right]] += 1
            maxOccurance = getMax(hashmap)

            while (right - left + 1) - maxOccurance > k:
                hashmap[s[left]] -= 1
                left += 1                     
            
            ans = max(ans, right - left + 1)

        return ans





        