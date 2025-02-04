class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashmap = Counter(s)

        
        ans = ""
        for char in order:
            if char in hashmap:
                ans += char * hashmap[char]
                hashmap.pop(char)
        
        for key in hashmap:
            ans += key * hashmap[key]

        return ans
        
        