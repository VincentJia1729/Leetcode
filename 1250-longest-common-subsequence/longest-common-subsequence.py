# text1 = "abcde"
# text2 = "ace"
# i indexes the rows, j indexes the columns
# (i,j) this is standard

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1) ]

        for i in range(len(text1) - 1,-1,-1): # the bottom row going to the top row (ignoring most bottom row of all 0's) 
            for j in range(len(text2)-1, -1,-1): # right column going to the the left column
            # ignoring right most column of all 0's 
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1] # this is possible because dp[i+1][j+1] = 0 due to the edges being initialized as 0
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j]) # dp[i][j+1] -> look to the cell to the right
                    # dp[i+1][j] -> look to the cell directly below
        return dp[0][0]
    