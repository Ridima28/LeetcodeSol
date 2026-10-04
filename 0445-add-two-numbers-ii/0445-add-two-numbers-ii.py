# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        def reverse(head):
            current = head
            prev = None 
            while current:
                next_node = current.next  # Store next node
                current.next = prev       # Reverse pointer
                prev = current            # Move prev forward
                current = next_node   
            return prev
    
        reverse_l1 = reverse(l1)
        reverse_l2 = reverse(l2)

        carry = 0
        dummy = ListNode(0)
        curr = dummy
        while reverse_l1 is not None or reverse_l2 is not None or carry !=0:
            total = carry

            if reverse_l1:
                total += reverse_l1.val
                reverse_l1 = reverse_l1.next
            if reverse_l2:
                total += reverse_l2.val
                reverse_l2 = reverse_l2.next 
            digit = total%10 
            carry = total//10 

            curr.next = ListNode(digit)
            curr = curr.next

        res = reverse(dummy.next)
        return res