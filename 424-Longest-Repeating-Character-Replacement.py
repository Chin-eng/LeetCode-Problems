class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        hashmap = defaultdict(int)
        
        left , ans = 0, float('-inf')
        for right in range(len(s)):
            hashmap[s[right]] += 1

            while (right - left + 1) - max(hashmap.values()) > k:
                hashmap[s[left]] -= 1
                left += 1                     
            
            ans = max(ans, right - left + 1)

        return ans





        