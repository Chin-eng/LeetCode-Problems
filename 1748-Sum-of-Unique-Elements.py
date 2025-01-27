class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1
        
        ans = []

        for key in hashmap:
            if hashmap[key] == 1:
                ans.append(key)
        
        return sum(ans)




        