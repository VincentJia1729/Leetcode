# Neetcode recursion solution
# if s1 = "226"
# then dp = {3: 1}

# this question requires a bit of finesse

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1} # notice that the value of the longest length is 1
        # this is our base case

        def dfs(i):
            if i in dp:
                return dp[i] # this prevents repeated work because we will keep adding to dp, we can just search up the previously stored value
            if s[i] == "0": # to prevent illegal cases of having "0" or like "06"
                return 0

            res = dfs(i + 1) # notice how we only increment by 1, when dfs "pops" the call stack
            # then we will do the 2 jumps
            if (i+ 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))): # if 2 jump is valid
                res += dfs(i+2) # add to the previous dfs(i+1), notice how dfs(i+1) stores all the paths with 1 jumps
                # this is because we do the path will all 1 jumps first, and add the paths with "2" jumps later
            dp[i] = res # dp[i] will overwrite the old value at key i, however, we will never overwrite so this issue will not come up
            return res
        return dfs(0)

# dp looks like this
# notice how dfs(0) will return dp[0]. This is because dp[i] = res and we return res
# dp = {
#   3: 1,
#   2: 1,
#   1: 2,
#   0: 3
# }
