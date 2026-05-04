"""
Set l = 0
iterate over the array with r
if price at r is lower than price at l
assign the value of r to l
at other points, compute profit and compare with max_profit
return max_profit
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0

        for r, price in enumerate(prices):
            if price < prices[l]:
                l = r
            else:
                max_profit = max(max_profit, price - prices[l])

        return max_profit
