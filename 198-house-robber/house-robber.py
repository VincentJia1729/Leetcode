class Solution:
    def rob(self, nums: List[int]) -> int:
        nums += [0]*2
        # as the robber, you can either single jump, or double jump
        for i in range(len(nums) - 5, -1, -1):
            nums[i] += max(nums[i+2], nums[i+3])
        return max(nums[0], nums[1])