class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        old_to_new = {} # dictionary that stores the old node as the key, and the new node as the value

        def dfs(node):
            if node in old_to_new: # if "node" is already a key in "old_to_node"
                return old_to_new[node] # return the value
            copy = Node(node.val)
            old_to_new[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None