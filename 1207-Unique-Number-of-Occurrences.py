class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        hashmap = defaultdict(int)

        for num in arr:
            hashmap[num] += 1
        
        hashset = set(hashmap.values())
        
        return len(hashmap.values()) == len(hashset)


        