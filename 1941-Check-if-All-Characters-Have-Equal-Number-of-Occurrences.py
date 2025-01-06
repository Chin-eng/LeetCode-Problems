class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hashmap = defaultdict(int)
        for letter in s:
            hashmap[letter] += 1
        
        frequences = hashmap.values()

        return len(set(frequences)) == 1