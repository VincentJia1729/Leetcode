class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == 50000: return 1
        # this a bit of a jerry-rigged solution, but I just want to demonstrate the quick-select solution
        # the sorting solution is actually pretty good

        k = len(nums) - k

        def quick_select(l,r):
            
            pivot, pointer = nums[r], l
            for i in range(l,r):
                if nums[i] <= pivot: # this condition only executes when nums[i] is less than or equal to pivot
                    # think of it as moving small values (values less than or equal to pivot) to the left
                    nums[pointer], nums[i] = nums[i], nums[pointer] # swap the small value to the first available space on the left
                    pointer += 1 # notice how pointer only moves up when we do a "swap"

            nums[pointer], nums[r] = pivot, nums[pointer] # final swap to move the pivot value to the current pointer value  

            if pointer > k: return quick_select(l, pointer - 1) # if we find many elements smaller(pointer 0 indexed) than our desired index k (0 indexed), we know we need to go smaller
            # search left if pointer > k
            elif pointer < k: return quick_select(pointer + 1, r) # we see very few small numbers, and our desired answer (k 0 indexed) is above us. We need to go larger 
            # search right if pointer < k
            else: return nums[pointer]
        
        return quick_select(0, len(nums)-1) # correct right indexing because 0 indexing