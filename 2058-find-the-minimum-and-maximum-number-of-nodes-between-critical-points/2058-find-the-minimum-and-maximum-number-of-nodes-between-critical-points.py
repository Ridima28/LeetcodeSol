# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode | None) -> list[int]:
        #local_min = big->small->big
        #localmaxima = small->big->small
        #mindistance = min(localmin) - min(localmax)
        #maxdistance = min(localmin) - max(localmax)

        cp = []

        count = 1
        curr = head
        prev = None
        while curr.next is not None: 
            if prev is not None:
                prev_val= prev.val
                curr_val  = curr.val
                next_val = curr.next.val

                if prev_val > curr_val and curr_val<next_val: #local_min
                    cp.append(count)
                elif prev_val<curr_val and curr_val >next_val: #local_max
                    cp.append(count)


            prev = curr
            curr = curr.next
            count +=1

        if len(cp) < 2:
            return [-1, -1]

        minimumdistance = float('inf')
        maximumdistance = cp[-1] - cp[0]

        for i in range(1,len(cp)):
            minimumdistance = min(minimumdistance, cp[i] - cp[i-1])

        return [minimumdistance, maximumdistance]