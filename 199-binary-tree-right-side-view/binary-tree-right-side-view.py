class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            level_size = len(q)
            rightmost = None

            for i in range(level_size):
                node = q.popleft()
                rightmost = node.val  # don't store the list, just store the most recent node

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(rightmost)

        return result