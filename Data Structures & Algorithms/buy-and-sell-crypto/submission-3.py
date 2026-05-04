"""
iterate over the array
assign the current element to buy_price if it is SMALLER
in the next iteration, check profit
compare with max profit
return max profit
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = prices[0]

        for price in prices:
            max_profit = max(price - buy_price, max_profit)
            buy_price = min(price, buy_price)

        return max_profit
