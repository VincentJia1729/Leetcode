# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    
    def isSubtree(self, root, subRoot):

        if not subRoot: # subRoot is NULL. subRoot does not change over time
           return True
        
        if not root: # root is NULL
            return False 
        
        if self.is_same_tree(root, subRoot): # if same tree
            return True
        
        return  (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)) # look at children
        # if at any point any child is True, then the whole return evaluates to true

    def is_same_tree(self, p, q):

    # base cases 
    # p is the root of the first tree
    # q is the root of the second tree

        if not p and not q: # if both nodes are Null, then they are the same
            return True
        
        if not p or not q: # we already checked that both nodes are NULL
            # but this bottom case catches the case where only one of p or q is Null
            return False

        if p.val != q.val: # if the values in p and q are not the same
            return False
    
    # check the children to see if they are the same
        return (self.is_same_tree(p.left, q.left)
            and self.is_same_tree(p.right, q.right))

    
    

        