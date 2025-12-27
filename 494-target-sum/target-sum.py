

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i,t): # i is the index of nums, "t" is the amount we currently have
            if i == len(nums): # if we've used all the possible nums in our list
                return 1 if t == target else 0
            if (i,t) in dp: # if you've seen this combination before
                return dp[(i,t)]
            dp[(i,t)] = dfs(i+1, t + nums[i]) + dfs(i+1, t - nums[i])
            return dp[(i,t)]
        return dfs(0,0)