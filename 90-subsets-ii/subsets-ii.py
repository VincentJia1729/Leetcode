class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        subset = []
        res = []

        def dfs(i):
            # let i be our index
            if i == len(nums):
                res.append(subset.copy())
                return 
            

            val = nums[i]
            # basic framework
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()

            # but we have to be clever to skip duplicates

            j = i+1
            while j < len(nums) and nums[j] == val:
                j +=1
            dfs(j)
        dfs(0)
        return res