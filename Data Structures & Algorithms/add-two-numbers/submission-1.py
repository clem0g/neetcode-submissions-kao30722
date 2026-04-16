# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        num1 = ""
        while curr:
            num1 += f"{curr.val}"
            curr = curr.next
        num1 = num1[::-1]
        num1 = int(num1)

        curr2 = l2
        num2 = ""
        while curr2:
            num2 += f"{curr2.val}"
            curr2 = curr2.next
        num2 = num2[::-1]
        num2 = int(num2)

        total = num1 + num2
        total = str(total)
        total = total[::-1]

        head = ListNode(int(total[0]))
        currn = head
        for i in range(1,len(total)):
            new = ListNode(int(total[i]))
            if currn:
                currn.next = new
                currn = currn.next
        

        return head 
