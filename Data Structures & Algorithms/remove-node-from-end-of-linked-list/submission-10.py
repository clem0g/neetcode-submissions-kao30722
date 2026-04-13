# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count+=1
            curr = curr.next

        if count == 1:
            return None  

        find = count - n
        if find == 0:
            return head.next

        num = 0
        remove = head
        while remove:
            if num == find:
                prev.next = remove.next
            num += 1
            prev = remove
            remove = remove.next
        return head



    