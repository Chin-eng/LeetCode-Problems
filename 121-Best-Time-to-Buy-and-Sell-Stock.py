class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        highest, ans = float(\-inf\), 0
        for right in range(len(prices)):
            highest = max(highest, prices[right])
            while left < right and prices[right] < prices[left]:
                highest = float(\-inf\)
                left += 1
            ans = max(ans, highest - prices[left])
        return ans
        