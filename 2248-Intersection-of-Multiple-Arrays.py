class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        hashmap = defaultdict(int)

        for num in nums:
            for element in num:
                hashmap[element] += 1
        
        ans = set()

        for num in nums:
            for element in num:
                if hashmap[element] == len(nums):
                    ans.add(element)
        
        return sorted(ans)