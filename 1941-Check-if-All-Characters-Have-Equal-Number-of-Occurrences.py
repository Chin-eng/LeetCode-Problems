class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hashmap = defaultdict(int)
        for letter in s:
            hashmap[letter] += 1

        count = hashmap[s[0]]
        
        for key in hashmap:
            if hashmap[key] != count:
                return False

        return True