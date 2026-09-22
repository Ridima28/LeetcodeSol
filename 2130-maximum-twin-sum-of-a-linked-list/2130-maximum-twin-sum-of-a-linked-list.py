# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        # 5421
        # 1245

        # 5+1
        # 4+2

        # seen = ((5,1)(4,2)(2,4))

        # seen = ((1,5), (2,4)) 
        temp = head
        values = []
        while temp is not None:
            values.append(temp.val)
            temp = temp.next

        
        prev = None
        curr = head

        while curr:
            next_node = curr.next      # save next
            curr.next = prev           # reverse link
            prev = curr                # move prev forward
            curr = next_node           # move curr forward

        #prev is the reversed linked list (1,2,4,5)
        temp1 = values
        temp2 = prev

        seen = set()
        count = 0
        i = 0


        while i<len(values) and temp2 is not None:
            key = tuple(sorted((temp1[i], temp2.val)))
            if key not in seen:
                count = max(count, temp1[i]+temp2.val)
                seen.add(key)

            i+=1
            temp2 =temp2.next

        return count
