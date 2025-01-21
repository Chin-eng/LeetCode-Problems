class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        hashmap = defaultdict(list)

        for num in nums:
            digit_sum = sum([int(char) for char in str(num)])
            hashmap[digit_sum].append(num)
        
        ans = float("-inf")

        for value in hashmap.values():
            if len(value) >= 2:
                largest_two = sorted(value, reverse=True)[:2]
                ans = max(ans, sum(largest_two))

        return ans if ans != float("-inf") else -1
        