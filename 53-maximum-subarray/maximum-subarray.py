

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0] # start with the first element
        cur_sum = 0

        for n in nums:
            if cur_sum < 0: # we will add the elements from left to right
                cur_sum = 0 # if we go negative, we reset the counter
            cur_sum += n # add the next right element
            max_sub = max(max_sub, cur_sum) # keep track of the largest sum so far
        return max_sub