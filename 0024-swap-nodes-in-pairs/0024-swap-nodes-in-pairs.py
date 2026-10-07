# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            next_pairs = curr.next.next 
            second = curr.next
            
            second.next = curr
            curr.next = next_pairs
            prev.next = second

            prev = curr
            curr = next_pairs

        return dummy.next
