# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head

        for i in range(k-1):
            curr = curr.next


        fast = curr
        slow = head

        while fast.next: 
            fast = fast.next
            slow = slow.next 

        curr.val , slow.val = slow.val , curr.val

        return head