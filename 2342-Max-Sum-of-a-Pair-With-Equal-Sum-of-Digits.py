class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        hashmap = defaultdict(list)

        for num in nums:
            digit_sum = sum([int(char) for char in str(num)])
            hashmap[digit_sum].append(num)
        
        print(hashmap)

        ans = float("-inf")

        for value in hashmap.values():
            if len(value) >= 2:
                array = sorted(value)
                sum_array = array[-1] + array[-2]
                ans = max(ans, sum_array)

        return ans if ans != float("-inf") else -1
        