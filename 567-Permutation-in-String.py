class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1_hashmap = Counter(s1)
        s2_hashmap = Counter(s2[:len(s1)])

        if s1_hashmap == s2_hashmap: return True
        left = 0
        for right in range(len(s1), len(s2)):
            s2_hashmap[s2[right]] += 1
            s2_hashmap[s2[left]] -= 1

            if s2_hashmap[s2[left]] == 0:
                s2_hashmap.pop(s2[left])

            left += 1

            if s1_hashmap == s2_hashmap:
                return True

        return False
        