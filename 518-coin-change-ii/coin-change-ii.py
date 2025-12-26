class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(i,a): # a is the amount of value in the coins we currently have
            if a == amount:
                return 1
            if a > amount: # if you have gone over the amount you want to meet
                return 0  
            if i  == len(coins): # if you have already used all the coins (exceeded the index of the list)
                return 0
            if (i,a) in dp: # if you have seen (i,a) before
                return dp[(i,a)]
            dp[(i,a)] = dfs(i, a + coins[i]) + dfs(i+1, a) # two choices
            # dfs(i, a + coins[i]), stay using the same coin
            # dfs(i+1, a), move on to the next coin
            return dp[(i,a)]
        return dfs(0,0)