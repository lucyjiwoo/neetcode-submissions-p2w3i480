class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        max_r = 0
        for i in reversed(range(len(prices))):
            if i == len(prices) -1:
                continue
            max_r = max(max_r, prices[i+1])
            max_profit = max(max_profit, max_r-prices[i])
        return max_profit
        