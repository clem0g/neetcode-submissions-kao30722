# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        if not head:
            return False
        elif current.next == None:
            return False
        elif current.next.next == None:
            return False
        else:
            slow = current.next
            fast = current.next.next
            while fast.next != None and fast.next.next != None:
                if fast == slow:
                    return True
                slow = slow.next
                fast = fast.next.next
            return False