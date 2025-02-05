class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if set(word1) != set(word2): return False

        word1_count = Counter(word1)
        word2_count = Counter(word2)

        word1_count_values = Counter([v for v in word1_count.values()])
        word2_count_values = Counter([v for v in word2_count.values()])             
        
        return (len(word1) == len(word2) and set(word1) == set(word2)) and word1_count_values == word2_count_values

        
        

        