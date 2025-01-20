class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for string in strs:
            sorted_string = \\.join(sorted(string))
            hashmap[sorted_string].append(string)
        
        ans = []

        for value in hashmap.values():
            ans.append(value)

        return ans