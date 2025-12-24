class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buying): # buying state is True if you are buying, False if you are selling
            if i >= len(prices): # if you have gone past the last day, remember i starts at 0
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)] # return the value of dp[(i,buying)] if we have already calculated it

            cooldown = dfs(i + 1, buying) # keep the current buying state without making any action 
            if buying: # if buying == True
                buy = dfs(i+1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown) 
            else: # if buying == False
                sell = dfs(i+2, not buying) + prices[i] # change False back to True
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        
        return dfs(0, True)