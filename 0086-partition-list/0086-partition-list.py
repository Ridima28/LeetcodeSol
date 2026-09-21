# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        less_target = ListNode(0) #head
        greater_target = ListNode(0)

        less = less_target #pointers
        greater = greater_target


        curr = head
        while curr!=None:
            if curr.val <x:
                less.next = curr
                less = less.next

            else:
                greater.next = curr
                greater = greater.next

            curr = curr.next 

        less.next = greater_target.next
        greater.next = None

        return less_target.next