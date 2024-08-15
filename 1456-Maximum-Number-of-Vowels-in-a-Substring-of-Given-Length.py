class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel ={'a', 'e', 'i', 'o', 'u'}
        left, count, res = 0,0,0

        for right in range(len(s)):
            count += 1 if s[right] in vowel else 0
            if right - left + 1 > k:
                count -= 1 if s[left] in vowel else 0
                left += 1
            res = max(count, res)
        return res