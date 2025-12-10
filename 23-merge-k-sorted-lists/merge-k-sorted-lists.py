class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1: # we will decrement len(lists) is a clever "halving way"
            temp_lists = [] # if we originally have [l1, l2, l3, l4]
            # after one round of merging, we have [[l1, l2], [l3,l4]] where [l1,l2] and [l3,l4] are a merged list

            for i in range(0, len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                temp_lists.append(self.merge_two_lists(l1,l2))
            lists = temp_lists # this is how we decrement lists
        return lists[0] # return the head of the linked list
    
    # remember how to merge just 2 lists
    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode() # technique to avoid annoying edge case of one of input ListNodes being empty
        tail = dummy # this tail will be moved forward

        while list1 and list2: # while both the ListNodes in list1 and list2 are not NULL
            if list1.val <= list2.val:
                tail.next = list1 # move tail to point to memory address of the current ListNode of list1
                list1 = list1.next # move the pointer of list1 up
            else:
                tail.next = list2 # move the tail to point to memory address of the current ListNode of list2
                list2 = list2.next # move the pointer of list2 up
            tail = tail.next # move the tail pointer of tail up

        if list1 is not None: # this means that list2 has run out
            tail.next = list1

        elif list2 is not None: # this means that list1 has run out
            tail.next = list2

        # tail.next = list1 if list1 is not None else list2
        # this is a more condensed way to write the "if ... elif" above
        
        return dummy.next
    