# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Check if list is empty
        #Use a counter to know node to remove
        # If list is shorter than counter remove the first node
        # Re route the node and return list

        if not head:
            return head

        if not head.next:
            return None 
        
        curr= head
        count = 1
        lst = []

        while curr.next:
            if count == n:
                remove = curr
                replace = curr.next.next 
            lst.append(curr)
            curr = curr.next
            count += 1

        if len(lst) == n:
            return head.next
        else:
            temp = remove
            remove.next = None
            remove.next = replace 

            return head
        
        

