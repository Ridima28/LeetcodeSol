# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        curr = head
        for i in range(k):
            if not curr :
                return head 
            curr = curr.next

        prev = None
        curr = head

        for _ in range(k):
            nxt = curr.next      # save next
            curr.next = prev     # reverse link
            prev = curr          # move prev forward
            curr = nxt           # move curr forward



        head.next = self.reverseKGroup(curr, k)
        return prev