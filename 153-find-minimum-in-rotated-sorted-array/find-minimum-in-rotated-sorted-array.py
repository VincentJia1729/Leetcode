class Solution:
    def findMin(self, nums: List[int]) -> int:

        result = nums[0] #just set arbitrarily to the first element of the array

        l , r = 0, len(nums) - 1
        
        while l <= r:
            if nums[l] < nums[r]: # this means our array is currently sorted
                result = min(result, nums[l])
                break
        
            m = (l + r) // 2
            result = min(result, nums[m])
        
            if nums[m] >= nums[l]: # Search Right because inflection point not on left side
                l = m+1 # move left pointer to the right
            else:# Search left because nums[m] < nums[l] if nums[l] is bigger this mean inflection point is on the left
                r = m -1 # move right pointer to the left

        return result
            