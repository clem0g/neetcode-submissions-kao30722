# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create the dummy anchor node and the tail pointer
        dummy = ListNode()
        tail = dummy
        
        # Traverse both lists as long as NEITHER is empty
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            # Move the tail pointer forward so it's ready for the next node
            tail = tail.next
            
        # If one list runs out before the other, attach the remaining nodes
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        # Return the actual head of the new list, skipping the dummy 0
        return dummy.next