# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isEvenOddTree(self, root: TreeNode | None) -> bool:

        if not root:
            return True 
        
        que = deque([root])

        count = 0

        while que:
            
            prev = float('-inf') if count % 2 == 0 else float('inf')

            for i in range(len(que)):
                node = que.popleft()

                if count %2 == 0:

                    if node.val%2 == 0 or node.val<=prev:
                        return False
                else:
                    if node.val%2 != 0 or node.val>=prev:  
                        return False
                        
                prev = node.val

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            count +=1 

        return True

        
