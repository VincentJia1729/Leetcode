# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q: # if both nodes are Null, then they are the same
                return True
            
        if not p or not q: # we already checked that both nodes are NULL
            # but this bottom case catches the case where only one of p or q is Null
            return False

        if p.val != q.val: # if the values in p and q are not the same
            return False
        
        # check the children to see if they are the same
        return (self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right))