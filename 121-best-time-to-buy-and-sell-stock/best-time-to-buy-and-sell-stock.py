class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        r = 1 # left represents buy at this price , right represents sell at this price

        while r < len(prices): # in our case r would max out at 5, len(prices) is 6 because 1-indexed

            # are we checking to see if we are profitable
            if min_price < prices[r]:
                profit = prices[r] - min_price
                max_profit = max(max_profit, profit)
            else:
                min_price = prices[r] # shift left to new lowest point
            r += 1
        return max_profit