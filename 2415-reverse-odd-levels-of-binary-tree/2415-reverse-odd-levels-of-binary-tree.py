# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def reverseOddLevels(self, root: TreeNode | None) -> TreeNode | None:

        que = deque([root])
        count = 0 
        while que:
            level = []

            for i in range(len(que)):
                
                node = que.popleft()
                level.append(node)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                
            if count%2 != 0 :
                left = 0
                right = len(level) -1

                while left< right:
                    level[left].val, level[right].val = level[right].val, level[left].val 

                    left+=1
                    right -=1
            count +=1 
        return root