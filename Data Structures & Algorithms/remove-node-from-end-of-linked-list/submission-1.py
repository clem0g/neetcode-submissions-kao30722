# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Optimal - Slow & Fast Pointers
        slow, fast = head, head
        removed = ListNode(-1, head)
        prev = removed

        # Advance fast n positions away from slow
        for n in range(n - 1):
            fast = fast.next
        
        # Now start going 1 by 1, slow and fast
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next

        # End reached, slow is now the nth item from the end, simply cut it out
        prev.next = slow.next
        
        return removed.next