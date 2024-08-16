class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", 'e', 'i', 'o', 'u'}

        left, result, count = 0, 0, 0

        for right in range(len(s)):
            count += 1 if s[right] in vowels else 0
            if right - left + 1 > k:
                count -= 1 if s[left] in vowels else 0
                left += 1 
            result = max(count, result)
        return result

        
        