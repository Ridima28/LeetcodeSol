# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        
        que = deque([(root,0)])
        ans  = 0
        if root is None:
            return 0

        while que:
            
            first  = que[0][1]
            last = que[-1][1]

            ans  = max(ans, last-first+1)

            for _ in range(len(que)):

                node,index =  que.popleft()

                if node.left:
                    que.append((node.left, 2*index+1))
                
                if node.right:
                    que.append((node.right, 2*index+2))


        return ans