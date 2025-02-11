class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minCost = prices[0]
        profit = 0 

        for price in prices:
            profit = max(profit, price - minCost)
            minCost = min(minCost, price)
        
        return profit
        