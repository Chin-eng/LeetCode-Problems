class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def find_unique_char_number(s):
            return len(set(s))
        
        unique_char_number = find_unique_char_number(s)
        result = 0

        for char in range(1, unique_char_number + 1):
            frequency_count = [0] * 26
            right = 0
            left = 0
            unique_char_at_least_k = 0
            unique_char = 0

            while right < len(s):
                if unique_char <= char:
                    index = ord(s[right]) - ord(\a\)
                    if frequency_count[index] == 0:
                        unique_char += 1
                    frequency_count[index] += 1
                    if frequency_count[index] == k:
                        unique_char_at_least_k += 1
                    right += 1
                else:
                    index = ord(s[left]) - ord(\a\)
                    if frequency_count[index] == k:
                        unique_char_at_least_k -= 1
                    frequency_count[index] -= 1
                    if frequency_count[index] == 0:
                        unique_char -= 1
                    left += 1
                
                if unique_char == char == unique_char_at_least_k:
                    result = max(result, right - left)          

        return result

        
        