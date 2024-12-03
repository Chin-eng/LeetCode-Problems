class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = "thequickbrownfoxjumpsoverthelazydog"
        seen1 = set()
        for s in sentence:
            seen1.add(s)
        
        seen2 = set()
        
        for s in letters:
            seen2.add(s)
        
        return len(seen2) == len(seen1)


        

        