class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        hashmap = defaultdict(list)

        def get_digit_sum(num):
            sum_value = 0
            while num:
                sum_value += num % 10
                num //= 10
            return sum_value

        for num in nums:
            digit_sum = get_digit_sum(num)
            hashmap[digit_sum].append(num)
        
        ans = float("-inf")

        for value in hashmap.values():
            if len(value) >= 2:
                largest_two = sorted(value, reverse=True)[:2]
                ans = max(ans, sum(largest_two))

        return ans if ans != float("-inf") else -1