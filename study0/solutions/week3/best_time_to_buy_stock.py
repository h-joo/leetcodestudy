class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(price, min_price)

        return max_profit
