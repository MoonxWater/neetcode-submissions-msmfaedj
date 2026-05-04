'''
iterate over the array 
assign the current element to buy_price if it is smaller
in the next iteration, check profit
compare with max profit
return max profit
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        max_profit = profit = 0
        buy_price = prices[0]

        for price in prices:
            profit = price - buy_price
            max_profit = max(profit, max_profit)

            buy_price = min(price, buy_price)

        return max_profit

