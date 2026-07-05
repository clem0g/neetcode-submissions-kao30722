# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lst = []
        for i in range (len(lists)):
            curr = lists[i]
            while curr:
                lst.append(curr.val)
                curr = curr.next
        sorted_lst = sorted(lst)
        if len(lst) == 0:
            return None
        else:
            head = ListNode(sorted_lst[0])
            curr = head
            i = 1
            while i < len(lst) and curr:
                curr.next = ListNode(sorted_lst[i])
                i += 1
                curr = curr.next
            return head
