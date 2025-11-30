class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:]) # notice that res from permute(nums[1:0]) becomes permute later on
        res = [] # so when we are clearing the result, the information is actually being saved in perm

        for p in perms:
            for i in range(len(p)+1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0]) # insert the current head of nums in all possible positions
                res.append(p_copy)
        return res