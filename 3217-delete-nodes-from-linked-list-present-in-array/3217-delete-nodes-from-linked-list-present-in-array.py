# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set(nums)

        curr = head 
        while head and head.val in nums:
            head = head.next

        while curr !=None:
            
            if curr.next and curr.next.val in seen:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head