# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def in_order(curr):
            if not curr:
                return None # by default return is "return None"
            in_order(curr.left)
            res.append(curr.val)
            in_order(curr.right)
    
        in_order(root)
        return res[k-1]