class Solution(object):
    def minWindow(self, s, t):
        \\\
        :type s: str
        :type t: str
        :rtype: str
        \\\
        Have, Need = 0, 0
        hashmap_t = defaultdict(int)
        for letter in t:
            hashmap_t[letter] += 1
            
        Need = len(hashmap_t)
        left, start, end, minSize = 0, 0, 0, float(\inf\)
        hashmap_s = defaultdict(int)
        
        for right in range(len(s)):
            if s[right] in hashmap_t:
                hashmap_s[s[right]] += 1
            if s[right] in hashmap_t and hashmap_s[s[right]] == hashmap_t[s[right]]:
                Have += 1

            while Have == Need:
                if right - left + 1 < minSize:
                    start, end = left, right
                    minSize = right - left + 1

                hashmap_s[s[left]] -= 1 
                
                if s[left] in hashmap_t and hashmap_s[s[left]] < hashmap_t[s[left]]:
                    Have -= 1

                left += 1

     
        return s[start:end+1] if minSize != float(\inf\) else \\
                
        