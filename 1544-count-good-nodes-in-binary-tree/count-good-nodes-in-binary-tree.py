# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_val):
            if not node:  # if node is null
                return 0
            
            res = 1 if node.val >= max_val else 0 # python ternary statement
            max_val = max(max_val, node.val)
            res += dfs(node.left, max_val) # do left branch first, not strictly necesary
            res += dfs(node.right, max_val)
            return res # after we break out of all the recursions, we will return our result
    
        return dfs(root, root.val)
        