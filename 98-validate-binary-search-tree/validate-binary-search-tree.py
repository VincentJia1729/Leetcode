# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check_valid(node, left_bound, right_bound):
            if not node: # if the node is null
                return True # an empty tree is technically a valid BST

            if not (node.val < right_bound and node.val > left_bound): # if node is not within valid boundary
                return False # return False
            
            return (check_valid(node.left, left_bound, node.val) and 
                    check_valid(node.right, node.val, right_bound)) # partition and do recursion on left and right nodes
    
        return check_valid(root, float("-inf"), float("inf"))