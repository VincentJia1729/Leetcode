# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: # eventually, something on the bottom of the tree like 4 will have 4.left and 4.right and both of those will be NULL
            return # just to break out of recursion. return is not used anywhere 

        # swap roots 
        # you can think of root as a "pointer" to a memory address
        # each root keeps it's specific initialization, so if 2 and 3 are swapped, all the subtrees below them are also moved along w 2 and 3
        temp = root.left
        root.left = root.right
        root.right = temp

        # recursive call
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root