# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        lst = []
        if not head:
            return head
        while curr:
            lst.append(curr)
            curr = curr.next
        if len(lst)%2 != 0:
            for i in range(len(lst)//2 + 1):
                    temp = lst[i].next
                    lst[i].next = lst[len(lst)-1 -i]
                    lst[len(lst)-1-i].next = temp
            lst[(len(lst)//2)].next=None
        else:
            for i in range(len(lst)//2):
                    temp = lst[i].next
                    lst[i].next = lst[len(lst)-1 -i]
                    lst[len(lst)-1-i].next = temp
            lst[len(lst)//2].next=None
        return head
            
                






        
 
   
        