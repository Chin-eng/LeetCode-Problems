class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        hashmap1  = {}
        hashmap2 = {}

        s_list = s.split()

        if len(pattern) != len(s_list): return False

        for i in range(len(pattern)):
            char, word = pattern[i], s_list[i]

            if ((char in hashmap1 and hashmap1[char] != word) or 
                word in hashmap2 and hashmap2[word] != char):
                return False

            hashmap1[char] = word
            hashmap2[word] = char
          
        return True
        