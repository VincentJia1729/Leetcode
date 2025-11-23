# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        # 1 -> 2 -> 3 -> 4 -> NULL
        dummy = ListNode(0, head) # create dummy for convenience to make numbers line up
        # 0 -> 1 -> 2 -> 3 -> 4 -> NULL
        left = dummy # left is at 0
        right = head # right is at 1

        while n > 0 and right: # this pushes right to 3
            right = right.next 
            n -= 1

        while right: # while right not NULL
            left = left.next
            right = right.next

        # change the link from the node before the node we want to delete 
        # this "deletes" the node from the list
        # the ListNode still technically exists in memory
        left.next = left.next.next
        
        return dummy.next