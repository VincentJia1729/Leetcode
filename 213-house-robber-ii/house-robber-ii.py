class Solution:
    def rob(self, nums: List[int]) -> int:
        # to be clever, we just use the original house robber 1 and adjust our starting position
        # if we have a list indexed 1 to n
        # then we need to check (2 to n) and (1 to n-1). This is because we have a choice
        # if we rob house n, we cannot rob house 1.
        # if we rob house 1, we cannot rob house n
        

        n = len(nums)
        # we need to worry about edge cases
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        amount1 = self.house_robber1(nums[: n-1])
        amount2 = self.house_robber1(nums[1:])
        return max(amount1, amount2)

    def house_robber1(self, nums: List[int]) -> int:
        nums += [0]*2
        # as the robber, you can either single jump, or double jump
        for i in range(len(nums) - 5, -1, -1):
            nums[i] += max(nums[i+2], nums[i+3])
        return max(nums[0], nums[1])