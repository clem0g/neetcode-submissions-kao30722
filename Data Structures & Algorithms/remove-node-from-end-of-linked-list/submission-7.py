# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Check if list is empty
        # Append the linked list to a list
        # Do the replace stuff for lst[len(lst) - n]
        # Re route the node and return list

        if not head:
            return head

        if not head.next:
            return None
            
        curr= head
        lst = []

        while curr:
            lst.append(curr)
            curr = curr.next

        temp = lst[len(lst) - n -1].next
        lst[len(lst) - n -1].next = None
        lst[len(lst) - n -1].next = temp.next

        return head
        
        

