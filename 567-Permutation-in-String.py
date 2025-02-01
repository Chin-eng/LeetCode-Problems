class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s2_hashmap = defaultdict(int)
        s1_hashmap = Counter(s1)

        def anagram(s1_hashmap, hashmap1):
            for key in s1_hashmap:
                if key not in hashmap1 or hashmap1[key] != s1_hashmap[key]:
                    return False
            return True

        left = 0
        for right in range(len(s2)):
            char_right = s2[right]
            s2_hashmap[char_right] += 1
            while right - left + 1 > len(s1):
                char_left = s2[left]
                s2_hashmap[char_left] -= 1
                if s2_hashmap[char_left] == 0:
                    s2_hashmap.pop(char_left)
                left += 1
            if len(s1_hashmap) == len(s2_hashmap) and anagram(s1_hashmap, s2_hashmap):
                return True
        
        return False

        
        



        
        

        