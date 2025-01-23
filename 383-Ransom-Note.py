class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap1 = defaultdict(int)
        hashmap2 = defaultdict(int)

        for s in magazine:
            hashmap1[s] += 1
        
        for s in ransomNote:
            hashmap2[s] += 1


        for key in hashmap2:
            if key not in hashmap1 or hashmap1[key] < hashmap2[key]:
                return False
                
        return True
        