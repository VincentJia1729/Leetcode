# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return [] # To catch edge case of [] entry
        result = []
        q = deque([root])

        while q: # while the q is still non-empty

            level_values = [] # another list
            for i in range(len(q)): # this is the current "layer of the tree"
                node = q.popleft()
                level_values.append(node.val)
                if node.left:
                    q. append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level_values)
        return result