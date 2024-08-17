class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        result, left, current_cost = 0, 0, 0
        for right in range(len(s)):
            current_cost += abs(ord(s[right]) - ord(t[right]))
            while current_cost > maxCost:
                current_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            result = max(result, right - left + 1)
        return result
       
       
       


        