class Solution:
    def frequencySort(self, s: str) -> str:

        hashmap1 = Counter(s)

        hashmap2 = defaultdict(list)

        for key, value in hashmap1.items():
            hashmap2[value].append(key)
            
        ans = []

        for i in range(len(s), 0, -1):
            for char in hashmap2[i]:
                ans.append(char * i)

        return \\.join(ans)
        
        