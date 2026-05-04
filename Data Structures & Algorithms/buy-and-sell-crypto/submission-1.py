"""
Set l and r = 0
iterate over the array with r
if price at r is lower than price at l
assign the value of r to l and move r forward
at other points, compute profit and compare with max_profit
return max_profit
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = 0
        max_profit = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
                continue
            
            max_profit = max(max_profit, prices[r] - prices[l])
            r += 1
            
        return max_profit
            