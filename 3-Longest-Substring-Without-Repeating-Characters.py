class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashset = set()

        ans, left = 0, 0

        for right in range(len(s)):
            
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1

            hashset.add(s[right])
            ans = max(ans, right - left + 1)

        return ans

        