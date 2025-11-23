# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(curr): # curr will be our root
            if not curr:
                return [True, 0] # balanced = true, height = 0
            # A node with no children is balanced and has height 0
            # when we get to a node with no children
            
            left_depth = dfs(curr.left)
            right_depth = dfs(curr.right)

            balanced = left_depth[0] and right_depth[0] and abs(left_depth[1] - right_depth[1] ) <=1

            return [balanced, 1 + max(left_depth[1],right_depth[1])]
    
        
        return dfs(root)[0]
        