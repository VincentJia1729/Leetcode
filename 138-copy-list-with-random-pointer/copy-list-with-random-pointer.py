"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        old_to_copy = {None: None} # idea is to have the keys be the original nodes, and the values to be the copied nodes
        # example 
        # old_to_copy = {A: A', B: B', C: C'} where A,B,C are originals and A', B', and C' are copies

        # first pass
        cur = head
        while cur: # not NULL
            copy = Node(cur.val) # create a new copy
            old_to_copy[cur] = copy # so we have a dictionary of copies (without any connections)
            cur = cur.next

        # second pass
        cur = head
        while cur:
            copy = old_to_copy[cur]
            copy.next = old_to_copy[cur.next] # remember that "cur" comes from the original linked list
            copy.random = old_to_copy[cur.random]
            cur = cur.next # move cur forward
        
        return old_to_copy[head]
        