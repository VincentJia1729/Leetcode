class Solution:
    def rob(self, nums: List[int]) -> int:
        nums += [0]*2
        # as the robber, you can either jump over 1 empty space, or jump over 2 empty spaces
        # Ex [1,2,3,4]
        # If you are at 1, you can either go to 3 or 4
        for i in range(len(nums) - 5, -1, -1):
            nums[i] += max(nums[i+2], nums[i+3])
        return max(nums[0], nums[1])