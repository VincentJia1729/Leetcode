class Solution:
    def search(self, nums: List[int], target: int) -> int:

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
            