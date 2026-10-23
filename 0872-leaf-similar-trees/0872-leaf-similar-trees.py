# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:


        def helper(root):
            res = []
            if not root:
                return
            stack = [root]

            while stack:
                node = stack.pop()

                if not node.left and not node.right:
                    res.append(node.val)
                else:
                    if node.left:
                        stack.append(node.left)

                    if node.right:
                        stack.append(node.right)

            return res

        return helper(root1) == helper(root2)