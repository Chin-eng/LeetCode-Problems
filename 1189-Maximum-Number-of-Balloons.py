class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = {
            "b" : 1,
            "a" : 1,
            "l" : 2,
            "o" : 2,
            "n" : 1
        } 

        hashmap = defaultdict(int)
        
        for letter in text:
            hashmap[letter] += 1

        ans = len(text)

        for key in balloon:

            ans = min(ans, hashmap[key]// balloon[key])
            
        return ans

        