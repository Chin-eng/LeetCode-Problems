class Solution:
    def frequencySort(self, s: str) -> str:

        hashmap1 = defaultdict(int)

        for string in s:
            hashmap1[string] += 1

        
        hashmap2 = defaultdict(list)

        for key in hashmap1:
            value = hashmap1[key]
            hashmap2[value].append(key)
            
        ans = []

        for i in range(len(s), 0, -1):
            for char in hashmap2[i]:
                ans.append(char * i)

        return \\.join(ans)
        
        