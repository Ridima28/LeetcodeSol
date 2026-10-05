# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        
        def reverse(node):
            curr =  node
            prev = None
            while curr:
                curr_next = curr.next
                curr.next = prev
                prev = curr
                curr = curr_next

            return prev
        
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next =  head

        before_left = dummy

        for i in range(left-1) :
            before_left = before_left.next
        
        left_node = before_left.next 

        right_node = left_node 

        for i in range(right-left):
            right_node = right_node.next

        after_right = right_node.next

        right_node.next = None

        reversed_list = reverse(left_node)

        before_left.next = reversed_list
        left_node.next = after_right

        return dummy.next