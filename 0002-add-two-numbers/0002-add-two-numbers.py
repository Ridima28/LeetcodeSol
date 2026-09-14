# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        dummy = ListNode(0)
        curr = dummy
        while l1 is not None or l2 is not None or carry !=0:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next 
            digit = total%10 
            carry = total//10 

            curr.next = ListNode(digit)
            curr = curr.next
        return dummy.next