class Solution:
    def search(self, nums: List[int], target: int) -> int:
    

        def binary_search(nums, target):
            low_pointer, high_pointer = 0, len(nums) - 1

            while low_pointer <= high_pointer:
                mid_pointer = (low_pointer + high_pointer) // 2
                
                if nums[mid_pointer] < target: # target on right block
                    low_pointer = mid_pointer + 1
                elif nums[mid_pointer] > target: # target on left block
                    high_pointer = mid_pointer - 1
                else:
                    return mid_pointer
            return -1

        result = nums[0] #just set arbitrarily to the first element of the array

        result_index = 0

        l , r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]: # this means our array is currently sorted
                    # if nums[l] < result, make m the new result_index 
                if nums[l] < result:
                    result_index = l
                result = min(result, nums[l])
                
                break

            m = (l + r) // 2
            
            # if nums[m] < result, make m the new result_index
            if nums[m] < result:
                result_index = m
            result = min(result, nums[m])
            

            if nums[m] >= nums[l]: # Search Right because inflection point not on left side
                l = m+1 # move left pointer to the right
            else:# Search left because nums[m] < nums[l] if nums[l] is bigger this mean inflection point is on the left
                r = m -1 # move right pointer to the left

        # return result, result_index
        # so we know "result" and "result_index"

        if result_index == 0: # there is no rotation
            final_result = binary_search(nums, target)
            return final_result

        if target >= nums[0]: # if target is greater than the left most element of nums, search Left of the pivot
            final_result = binary_search(nums[0:result_index],target)
            return final_result

        else: # if target is less than or equal to the left most most element of nums, serach Right of the pivot 
            final_result = binary_search(nums[result_index:],target) 
            if final_result != -1:
                final_result += result_index
            return final_result