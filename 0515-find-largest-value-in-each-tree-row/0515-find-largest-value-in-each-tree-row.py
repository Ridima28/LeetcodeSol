# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        
        def bfs(root):
            if root is None:
                return []
            que = [root]
            ans = []
            

            while que:
                maxi = float('-inf')

                for _ in range(len(que)):
                    node = que.pop(0)

                    maxi = max(maxi, node.val)

                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)

                ans.append(maxi)
            return ans
        return bfs(root)